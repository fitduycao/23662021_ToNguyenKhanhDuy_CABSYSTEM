"""Kiểm tra bộ API nhiều file: python validate.py (cần PyYAML và jsonschema).

Đây là kiểm tra cấu trúc/tham chiếu/ví dụ, không thay thế validator OpenAPI đầy đủ
hoặc kiểm thử backend.
"""
from pathlib import Path
import copy
import json
import re
import sys
import yaml
from jsonschema import Draft4Validator, FormatChecker

ROOT = Path(__file__).resolve().parent
DOCS = {}
REF_COUNT = 0
EXAMPLE_COUNT = 0

class UniqueKeyLoader(yaml.SafeLoader):
    pass

def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError('Duplicate YAML key: ' + str(key))
        result[key] = loader.construct_object(value_node, deep=deep)
    return result

UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)

def read(path):
    path = path.resolve()
    if path not in DOCS:
        DOCS[path] = yaml.load(path.read_text(encoding='utf-8'), Loader=UniqueKeyLoader)
    return DOCS[path]

def resolve_reference(ref, source):
    relative, _, fragment = ref.partition('#')
    path = (source.parent / relative).resolve() if relative else source
    if ROOT not in path.parents and path != ROOT:
        raise ValueError('Reference escapes deliverable: ' + ref)
    result = read(path)
    if fragment:
        if not fragment.startswith('/'):
            raise ValueError('Unsupported pointer ' + fragment)
        for key in fragment[1:].split('/'):
            result = result[key.replace('~1','/').replace('~0','~')]
    return result, path

def expand(value, source, stack=()):
    global REF_COUNT
    if isinstance(value, list):
        return [expand(v,source,stack) for v in value]
    if not isinstance(value,dict):
        return value
    if '$ref' in value:
        if len(value) != 1:
            raise ValueError('Ignored $ref siblings in OpenAPI 3.0: ' + str(value))
        key=(str(source),value['$ref'])
        if key in stack:
            raise ValueError('Circular reference ' + str(key))
        target, file = resolve_reference(value['$ref'],source)
        REF_COUNT += 1
        return expand(target,file,stack+(key,))
    return {k:expand(v,source,stack) for k,v in value.items()}

def json_schema(value):
    if isinstance(value,list):
        return [json_schema(v) for v in value]
    if not isinstance(value,dict):
        return value
    out = {k:json_schema(v) for k,v in value.items() if k not in ['nullable','example','readOnly','writeOnly','xml','discriminator','externalDocs','deprecated']}
    if value.get('nullable') and 'type' in out:
        out['type'] = [out['type'],'null']
    return out

def validate_example(schema, value, context):
    global EXAMPLE_COUNT
    schema = json_schema(schema)
    Draft4Validator.check_schema(schema)
    errors = list(Draft4Validator(schema, format_checker=FormatChecker()).iter_errors(value))
    if errors:
        raise ValueError(context + ': ' + '; '.join(e.message for e in errors))
    EXAMPLE_COUNT += 1

def scan_examples(value, context):
    if isinstance(value,list):
        for index,v in enumerate(value): scan_examples(v,f'{context}/{index}')
    elif isinstance(value,dict):
        if 'schema' in value and 'example' in value:
            validate_example(value['schema'],value['example'],context)
        elif 'type' in value and 'example' in value:
            validate_example(value,value['example'],context)
        for k,v in value.items(): scan_examples(v,context+'/'+k)

def no_secret_fields(value):
    if isinstance(value,dict):
        forbidden = {'password','accessToken','cardNumber','cvv','bankAccountNumber'}
        assert not forbidden.intersection(value.get('properties',{})), 'Secret response field'
        for v in value.values(): no_secret_fields(v)
    elif isinstance(value,list):
        for v in value: no_secret_fields(v)

def validate_document(doc, context):
    assert doc['openapi'] == '3.0.3'
    assert doc['info']['title'] and doc['info']['version']
    assert isinstance(doc['paths'],dict)
    ids = set()
    requirements = set()
    for path, item in doc['paths'].items():
        assert path.startswith('/')
        assert isinstance(item,dict)
        for method, op in item.items():
            assert method in {'get','post','put','patch','delete','options','head','trace'}
            fn=op['operationId']
            assert fn not in ids, 'Duplicate operationId: '+fn
            ids.add(fn)
            assert fn == op['x-function']
            assert op['summary'] and op['description'] and op['x-authorization']
            requirements.update(op['x-functional-requirements'])
            parameters=op.get('parameters',[])
            keys=[(p['name'],p['in']) for p in parameters]
            assert len(keys)==len(set(keys)), 'Duplicate parameters'
            path_params={p['name'] for p in parameters if p['in']=='path' and p.get('required') is True}
            assert set(re.findall(r'\{([^}]+)\}',path)) == path_params, path
            for p in parameters:
                assert p['in'] in ['path','query','header','cookie'] and 'schema' in p
            security=op.get('security',doc.get('security'))
            assert security is not None
            for scheme in security:
                for key in scheme:
                    assert key in doc['components']['securitySchemes']
            if method=='get': assert 'requestBody' not in op
            if 'requestBody' in op:
                assert op['requestBody']['required'] is True
                assert 'application/json' in op['requestBody']['content']
            assert any(code.startswith('2') for code in op['responses'])
            for code,res in op['responses'].items():
                assert re.fullmatch(r'[1-5][0-9][0-9]',code)
                assert res['description']
                if code=='204': assert 'content' not in res
                if code.startswith('2') and fn!='login':
                    no_secret_fields(res)
    scan_examples(doc,context)
    return ids,requirements

def main():
    files=sorted(ROOT.rglob('*.yaml'))
    # Mọi YAML đều được parse và mọi external reference đều được giải quyết.
    expanded={p:expand(read(p),p) for p in files}
    documents={p:d for p,d in expanded.items() if isinstance(d,dict) and 'openapi' in d}
    root_ids,fr=validate_document(documents[ROOT/'api.yaml'],'api.yaml')
    module_ids=set()
    for path,doc in documents.items():
        if path==ROOT/'api.yaml': continue
        ids,_=validate_document(doc,str(path.relative_to(ROOT)))
        assert not module_ids.intersection(ids), 'Duplicate operation across modules'
        module_ids.update(ids)
    assert root_ids==module_ids, 'Root/module operation mismatch'
    assert fr=={f'FR-{i:02d}' for i in range(1,28)}, 'FR coverage mismatch'
    schemas=expanded[ROOT/'common'/'schemas.yaml']
    for name,schema in schemas.items():
        Draft4Validator.check_schema(json_schema(schema))
    report={'status':'PASS','yamlFiles':len(files),'openapiEntryPoints':len(documents),'modules':len(documents)-1,
            'operations':len(root_ids),'schemas':len(schemas),'functionalRequirementsCovered':len(fr),
            'referenceResolutions':REF_COUNT,'exampleChecks':EXAMPLE_COUNT,
            'checks':['YAML parse and duplicate keys','All local $ref and JSON Pointer targets','Root/module consistency',
                      'Unique operationId and x-function','Path/query/header parameters','Security scheme references',
                      'Request and response examples against resolved schemas','No sensitive profile response fields',
                      'FR-01 through FR-27 coverage'],
            'limitations':['Custom structural checker, not a full OpenAPI meta-schema validator.',
                           'No running backend, no integration or load tests, no Swagger UI rendering test.',
                           'Business policies marked TBD remain unapproved.']}
    (ROOT/'VALIDATION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=True))

if __name__=='__main__':
    main()
