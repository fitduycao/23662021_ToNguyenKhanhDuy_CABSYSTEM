# CAB System — API theo Functional Requirements

Đây là **đặc tả API**, chưa phải mã backend hoặc dịch vụ đang chạy. Nguồn là FR-01 đến FR-27 trong `../srs.md`. Tài liệu tách theo module; không dồn định nghĩa tất cả API vào một file.

## Cách tổ chức

- `api.yaml`: tài liệu OpenAPI đầu mối, chỉ tham chiếu đường dẫn sang từng module bằng `$ref`.
- `<module>/api.yaml`: tài liệu OpenAPI riêng cho nhóm chức năng, có thể làm entry point riêng khi công cụ hỗ trợ tham chiếu file bên ngoài.
- `common/schemas.yaml`: cấu trúc request/response dùng chung, tách riêng schema đầu vào và đầu ra.
- `common/parameters.yaml`, `responses.yaml`, `security.yaml`: tham số, lỗi và xác thực dùng chung.
- `workflows/internal-functions.yaml`: chức năng nền như điều phối, tính cước, gửi thông báo, đối soát và audit; không phải endpoint công khai.
- `ENDPOINTS.md`: bảng từng API, tên function và mã FR.
- `TRACEABILITY.md`: kiểm tra bao phủ đủ 27 FR, phân biệt endpoint với xử lý nội bộ.
- `validate.py` và `VALIDATION.json`: bộ kiểm tra cấu trúc/tham chiếu/ví dụ và kết quả kiểm tra. Chạy `python validate.py` khi đã có PyYAML và jsonschema. Đây không phải validator OpenAPI đầy đủ hoặc kiểm thử backend.

`operationId` là tên function gợi ý cho backend, ví dụ `createUser`, `listUsers`, `getUserById`, `updateUser`, `deleteUser`. `x-function` nhắc lại tên này để dễ tra cứu. Đây không phải function đã được lập trình.

## Ví dụ nhóm User có CRUD

| Thao tác | Method và endpoint | Function |
|---|---|---|
| Create: tạo user khách hàng bởi vận hành | POST /users | createUser |
| Read: lấy danh sách | GET /users | listUsers |
| Read: lấy một user | GET /users/{userId} | getUserById |
| Update: sửa một phần hồ sơ | PATCH /users/{userId} | updateUser |
| Delete: vô hiệu hóa/xóa mềm | DELETE /users/{userId} | deleteUser |

Tự đăng ký dùng `POST /auth/register`; đăng ký tài xế dùng `POST /auth/drivers/register`; vận hành tạo tài xế dùng `POST /drivers`. `users` dùng mã tài khoản, còn `drivers` dùng mã hồ sơ tài xế; không mặc định hai mã giống nhau.

## Nội dung mỗi API

Mỗi operation có tên, mô tả chức năng, `operationId`, quyền, `x-functional-requirements`, path/query/header parameters khi có, request body khi cần, response schema/ví dụ, mã lỗi và mẫu cURL trong `x-codeSamples`. OpenAPI mô tả Content-Type qua `content.application/json`; Authorization được mô tả bằng `securitySchemes`.

Tài liệu dùng OpenAPI 3.0.3 và tham chiếu nhiều file. Giữ nguyên toàn bộ thư mục khi mở bằng công cụ có hỗ trợ external `$ref`. Không chỉ sao chép riêng nội dung `api.yaml` vào một editor không có các file còn lại. Có thể mở `users/api.yaml` làm entry point để chỉ xem nhóm User, nhưng vẫn phải giữ `common/` ở đúng vị trí. Nếu công cụ yêu cầu bundle một file, đó chỉ nên là bản xuất tạm; bộ nguồn vẫn tách module.

Các ví dụ cURL dùng cú pháp shell kiểu Bash; cần điều chỉnh dấu nháy/xuống dòng nếu dùng PowerShell. URL và token là minh họa, không phải môi trường thật.

## Quy ước và những quyết định còn mở

- Base URL minh họa: `https://api.cab.example.com/api/v1`. Chưa chọn hosting hoặc nhà cung cấp.
- Điện thoại/mật khẩu, UUID, trường hồ sơ, phân trang 20/tối đa 100, mô hình vai trò và quyền là đề xuất thiết kế, không phải chi tiết đã được Word chốt.
- `User.role` biểu diễn vai trò hồ sơ chính; quyền hiệu lực có thể dựa trên nhiều role assignment. Không dùng trường này để bỏ qua kiểm tra quyền phía máy chủ. Cơ cấu vai trò cần xác nhận ở TBD-11.
- PATCH chỉ nhận trường được phép và phải có ít nhất một trường; không cho client sửa role/status/amount qua payload hồ sơ hoặc đặt chuyến.
- DELETE user/driver/vehicle là **đề xuất mở rộng để thể hiện CRUD**, có `x-status: proposed-extension`. Đây là xóa mềm/vô hiệu hóa; chính sách lưu trữ, quyền và điều kiện phải được duyệt. Không cung cấp xóa chuyến, giao dịch hoặc audit chỉ để đủ bốn chữ CRUD.
- Đánh giá 1–5 và một đánh giá/chuyến là đề xuất TBD-10. Công thức cước, tiêu chí ghép, hủy, tiền mặt, thời hạn offer, retention, retry và chỉ số báo cáo vẫn theo TBD của SRS. Endpoint phụ thuộc chính sách chưa chốt không được thực hiện bằng mặc định tùy ý.
- Mọi tài nguyên phải kiểm tra quyền sở hữu bên cạnh vai trò. Filter/query không được mở rộng phạm vi dữ liệu. Không trả password/token trong hồ sơ hoặc audit.
- `Idempotency-Key` bắt buộc tại các lệnh có nguy cơ lặp. Lưu khóa/kết quả bền vững và xử lý đồng thời; thời hạn lưu phải được duyệt. Cơ chế này bổ sung cho khóa phân công/thanh toán theo nghiệp vụ, không thay thế chúng.
- Thanh toán `processing` chưa chắc thất bại; không tạo lần thu mới khi kết quả trước chưa rõ. Không lưu thông tin thẻ/tài khoản nhạy cảm. Xác nhận tiền mặt không được công khai cho mọi khách hàng.
- Webhook HMAC trong đặc tả là hợp đồng adapter đề xuất; phải thay/điều chỉnh theo nhà cung cấp thật. Không coi Bearer token khách hàng là bằng chứng thanh toán.
- FR-06/08/13/18/19/26 có phần chạy tự động ở máy chủ. Chúng được mô tả trong workflow và API kích hoạt/tra cứu; không tạo API công khai cho người dùng tự phân công, tự tính cước hoặc tự phát kết quả thanh toán.
- Thao tác hỗ trợ cụ thể ngoài ghi nhận/đóng sự cố vẫn cần TBD-11. Chưa có API sửa tùy ý trạng thái hoặc cước dưới danh nghĩa hỗ trợ.
- NFR về tải, bảo mật thực thi, cô lập lỗi và mở rộng chỉ có thể nghiệm thu khi có backend; đặc tả YAML không chứng minh hệ thống đã đáp ứng NFR.

## Nguồn tham khảo

- Yêu cầu dự án: `../srs.md`, được phân tích từ `Customer-Requirement.docx`.
- Cách trình bày: https://200lab.io/blog/api-document
- Chuẩn kỹ thuật nhiều file, operationId, schema và security: https://spec.openapis.org/oas/v3.0.3.html
