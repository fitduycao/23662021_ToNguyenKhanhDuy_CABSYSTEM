| Stakeholder (Bên liên quan) | Vai trò |
| :--- | :--- |
| **Ban Giám đốc (Management / Sponsor)** | Định hướng dự án, duyệt ngân sách/tiến độ (7 tuần), chốt các chính sách nghiệp vụ và theo dõi báo cáo doanh thu, hiệu quả hoạt động.[cite: 1] |
| **Khách hàng (Customer / Rider)** | Đăng ký/đăng nhập, tạo yêu cầu đặt xe, theo dõi chuyến đi theo thời gian thực, thực hiện thanh toán và đánh giá tài xế.[cite: 1] |
| **Tài xế (Driver)** | Cập nhật hồ sơ/phương tiện, bật trạng thái sẵn sàng, nhận/từ chối cuốc xe, chia sẻ vị trí GPS và cập nhật tiến trình chuyến đi.[cite: 1] |
| **Nhân viên Vận hành (Operations Staff)** | Giám sát các chuyến đi đang chạy, kiểm tra trạng thái tài xế, hỗ trợ xử lý sự cố/lỗi chuyến và tra cứu lịch sử giao dịch.[cite: 1] |
| **Nhân viên Quản trị Hệ thống (System Admin)** | Quản lý phân quyền tài khoản, giám sát bảo mật hệ thống và theo dõi nhật ký kiểm toán (audit log).[cite: 1] |
| **Cổng Thanh toán (Payment Gateway Provider)** | Đối tác bên thứ ba xử lý các giao dịch thanh toán điện tử an toàn, không để lộ thông tin thẻ nhạy cảm trên hệ thống.[cite: 1] |
| **Nhà cung cấp Thông báo (Notification Provider)** | Đối tác bên thứ ba hỗ trợ phát thông báo tự động (Push notification, SMS) tới khách hàng và tài xế.[cite: 1] |
| **Đội ngũ Kỹ thuật / Phát triển (Dev / QA Team)** | Thiết kế kiến trúc chịu tải, lập trình hệ thống theo yêu cầu và triển khai giải pháp trong thời hạn 7 tuần.[cite: 1] |
| **Chuyên viên Phân tích Nghiệp vụ (Business Analyst)** | Khảo sát, làm rõ các quy tắc còn thiếu (tính cước, tiêu chí tìm tài xế, hủy chuyến, timeout) và đặc tả yêu cầu cho đội kỹ thuật.[cite: 1] |



## Stakeholder Matrix - CAB System

quadrantChart
    title STAKEHOLDER MATRIX - CAB SYSTEM (Power vs Interest)
    x-axis "Mức độ Quan tâm Thấp (Low Interest)" --> "Mức độ Quan tâm Cao (High Interest)"
    y-axis "Quyền lực / Ảnh hưởng Thấp (Low Power)" --> "Quyền lực / Ảnh hưởng Cao (High Power)"
    quadrant-1 "QUẢN LÝ CHẶT CHẼ (Manage Closely)"
    quadrant-2 "GIỮ HÀI LÒNG (Keep Satisfied)"
    quadrant-3 "GIÁM SÁT TỐI THIỂU (Monitor)"
    quadrant-4 "CẬP NHẬT THÔNG TIN (Keep Informed)"
    "Ban Giám đốc ABC": [0.88, 0.92]
    "Đội ngũ BA": [0.92, 0.72]
    "Đội ngũ Kỹ thuật (Dev/QA)": [0.85, 0.65]
    "Cổng Thanh toán (Payment Gateway)": [0.38, 0.75]
    "Đối tác Thông báo (Notification)": [0.32, 0.58]
    "Khách hàng (Customer)": [0.88, 0.35]
    "Tài xế (Driver)": [0.90, 0.38]
    "Nhân viên Vận hành (Operations)": [0.82, 0.42]
    "Nhân viên Quản trị Hệ thống": [0.70, 0.48]





# CAB SYSTEM - CHUYỂN ĐỔI YÊU CẦU THÀNH MỤC TIÊU NGHIỆP VỤ & BUSINESS RULES

**Dự án:** Nền tảng đặt xe CAB System  
**Phiên bản:** MVP 1.0 (Kế hoạch triển khai 7 tuần)  
**Tác giả:** Senior Business Analyst  
**Ngày lập:** 06/09/2026  
**Trạng thái quy tắc:** `Confirmed` (Đã xác nhận) | `TBD` (To Be Determined - Chờ khách hàng làm rõ)

---

## 1. BẢNG CHUYỂN ĐỔI: TỪ YÊU CẦU KHÁCH HÀNG ĐẾN MỤC TIÊU NGHIỆP VỤ (MAPPING)

| Mã YC | Yêu cầu của Khách hàng | Mục tiêu Nghiệp vụ (Business Objective) | Mã Quy tắc liên quan (BR Code) |
| :--- | :--- | :--- | :--- |
| **CR-01** | Khách hàng và tài xế phải có tài khoản rõ ràng, an toàn để sử dụng ứng dụng. | Đảm bảo tính định danh, an toàn pháp lý và phân quyền chuẩn xác giữa các đối tượng người dùng. | `BR-AUTH-01`, `BR-AUTH-02` |
| **CR-02** | Khách hàng cần biết trước lộ trình di chuyển và giá tiền dự kiến trước khi quyết định gọi xe. | Minh bạch hóa thông tin chi phí để tăng tỷ lệ chuyển đổi đặt xe và giảm tỷ lệ hủy chuyến do bất ngờ về giá. | `BR-PRICING-01`, `BR-BOOKING-01` |
| **CR-03** | Hệ thống tự động tìm và kết nối cuốc xe đến tài xế phù hợp ở gần nhất một cách nhanh chóng. | Tối ưu hóa thời gian chờ đón xe của khách hàng (ETA) và giảm thiểu quãng đường di chuyển không tải của tài xế. | `BR-DISPATCH-01`, `BR-DISPATCH-02`, `BR-DISPATCH-03` |
| **CR-04** | Tài xế có quyền quyết định nhận hoặc bỏ qua chuyến xe được mời. | Tôn trọng tính chủ động của đối tác tài xế, đồng thời tự động tái điều phối để không làm gián đoạn yêu cầu của khách. | `BR-DISPATCH-02`, `BR-DISPATCH-04` |
| **CR-05** | Tiến trình chuyến đi (đón khách, đang đi, trả khách) phải được cập nhật minh bạch cho cả hai bên. | Nâng cao mức độ tin cậy, kiểm soát hành trình theo thời gian thực và làm căn cứ giải quyết tranh chấp. | `BR-STATE-01`, `BR-STATE-02` |
| **CR-06** | Hỗ trợ thanh toán thuận tiện bằng cả tiền mặt và phương thức điện tử khi chuyến đi hoàn thành. | Đảm bảo thu hồi đủ doanh thu chuyến xe, tối ưu dòng tiền và không làm giam giữ thời gian của tài xế. | `BR-PAY-01`, `BR-PAY-02`, `BR-PAY-03` |
| **CR-07** | Cho phép khách hàng phản ánh chất lượng phục vụ của tài xế sau mỗi chuyến đi. | Kiểm soát chất lượng dịch vụ của đội ngũ tài xế và làm cơ sở duy trì tiêu chuẩn vận hành nền tảng. | `BR-RATE-01` |
| **CR-08** | Nhân viên nội bộ có công cụ theo dõi, giám sát và can thiệp sự cố hoặc hủy cuốc bất thường. | Đảm bảo khả năng vận hành liên tục, xử lý sự cố kịp thời và bảo vệ quyền lợi của các bên liên quan. | `BR-OPS-01`, `BR-CANCEL-01` |

---

## 2. DANH MỤC QUY TẮC NGHIỆP VỤ (BUSINESS RULES - BR)

### Nhóm 1: Xác thực & Quản lý Tài khoản (BR-AUTH)

#### `BR-AUTH-01`: Định danh duy nhất theo vai trò
* **Mục tiêu:** Kiểm soát phân quyền và trách nhiệm pháp lý của từng nhóm người dùng.
* **Quy tắc:** Mỗi tài khoản đăng ký phải được gắn với một số điện thoại duy nhất. Tại một phiên làm việc (Session), một người dùng chỉ được hoạt động dưới đúng **01 vai trò (Role)**: Customer, Driver hoặc Operation Staff.
* **Trạng thái:** `Confirmed`.

#### `BR-AUTH-02`: Điều kiện kích hoạt đối tác Tài xế
* **Mục tiêu:** Đảm bảo tiêu chuẩn an toàn và tính hợp pháp của phương tiện tham gia nền tảng.
* **Quy tắc:** Tài khoản Driver chỉ được chuyển sang trạng thái hoạt động (`ACTIVE`) sau khi hồ sơ cá nhân (CMND/CCCD, Giấy phép lái xe, Đăng ký xe, Bảo hiểm bắt buộc) đã được Operation Staff xác thực thủ công thành công trên hệ thống quản trị.
* **Trạng thái:** `Confirmed`.

---

### Nhóm 2: Yêu cầu & Tạo Chuyến xe (BR-BOOKING)

#### `BR-BOOKING-01`: Ràng buộc thông tin khởi tạo cuốc xe
* **Mục tiêu:** Tránh các yêu cầu rác và đảm bảo đủ dữ liệu để tính toán lộ trình.
* **Quy tắc:** Để gửi yêu cầu đặt xe thành công, Customer bắt buộc phải cung cấp:
  1. Tọa độ điểm đón hợp lệ.
  2. Tọa độ điểm đến hợp lệ (khác tọa độ đón tối thiểu 100 mét).
  3. Lựa chọn loại phương tiện (Xe 4 chỗ, Xe máy...).
  4. Phương thức thanh toán mặc định cho chuyến đi.
* **Trạng thái:** `Confirmed`.

#### `BR-BOOKING-02`: Giới hạn số chuyến xe đồng thời
* **Mục tiêu:** Ngăn chặn đặt xe ảo và lạm dụng tài nguyên điều phối.
* **Quy tắc:** Tại một thời điểm, một Customer chỉ được phép có tối đa **01 chuyến xe đang hoạt động** (từ trạng thái `REQUESTED` đến `IN_PROGRESS`). Không được tạo cuốc mới khi cuốc hiện tại chưa hoàn thành hoặc chưa hủy.
* **Trạng thái:** `Confirmed`.

---

### Nhóm 3: Điều phối & Ghép chuyến (BR-DISPATCH)

#### `BR-DISPATCH-01`: Tiêu chí lọc Driver khả dụng
* **Mục tiêu:** Chỉ gửi tín hiệu mời cuốc cho tài xế thực sự sẵn sàng phục vụ.
* **Quy tắc:** Một Driver chỉ được đưa vào danh sách ứng viên nhận chuyến khi thỏa mãn đồng thời 4 điều kiện:
  1. Tài khoản ở trạng thái `ACTIVE`.
  2. Đang bật chế độ nhận việc (`ONLINE`).
  3. Đang không thực hiện bất kỳ chuyến xe nào khác (`is_busy = false`).
  4. Vị trí GPS được cập nhật trong vòng tối đa **60 giây** gần nhất.
* **Trạng thái:** `Confirmed`.

#### `BR-DISPATCH-02`: Quy tắc ưu tiên và Bán kính quét cuốc
* **Mục tiêu:** Rút ngắn tối đa thời gian chờ đón khách (ETA).
* **Quy tắc:** Hệ thống tự động quét các Driver khả dụng trong bán kính ban đầu tính từ điểm đón khách. Thứ tự mời cuốc được sắp xếp ưu tiên theo khoảng cách di chuyển từ vị trí tài xế đến điểm đón (ngắn nhất trước).
* **Trạng thái:** `TBD`.
* **Câu hỏi BA cần làm rõ:** 
  > *Bán kính quét ban đầu là bao nhiêu km (ví dụ: 3km)? Khi không tìm thấy tài xế, bán kính mở rộng thêm bao nhiêu km (ví dụ: 5km, 7km)? Ưu tiên tuyệt đối theo khoảng cách (ETA) hay có kết hợp điểm đánh giá sao (Rating) của tài xế?*

#### `BR-DISPATCH-03`: Thời hạn phản hồi nhận cuốc (Timeout)
* **Mục tiêu:** Tránh làm gián đoạn thời gian chờ của khách hàng khi tài xế không tương tác.
* **Quy tắc:** Khi nhận được tín hiệu mời chuyến, Driver có đúng **N giây** đếm ngược để bấm "Chấp nhận". Nếu Driver bấm "Từ chối" hoặc đồng hồ về 0 (Timeout), hệ thống lập tức loại trừ Driver này khỏi phiên tìm kiếm hiện tại và chuyển tiếp tín hiệu mời chuyến đến Driver thỏa mãn điều kiện tiếp theo.
* **Trạng thái:** `TBD`.
* **Câu hỏi BA cần làm rõ:** 
  > *Thời gian đếm ngược chính xác để tài xế phản hồi là bao nhiêu giây (ví dụ: 15 giây, 20 giây hay 30 giây)?*

#### `BR-DISPATCH-04`: Giới hạn tìm kiếm và Dừng cuốc xe
* **Mục tiêu:** Đóng luồng xử lý và thông báo dứt khoát cho khách khi thị trường không có nguồn cung.
* **Quy tắc:** Hệ thống tự động dừng tìm kiếm và chuyển trạng thái chuyến xe sang `NO_DRIVER_FOUND` khi:
  - Đã gửi lời mời qua tối đa **M tài xế liên tiếp** nhưng không ai nhận, HOẶC
  - Tổng thời gian tìm kiếm của cuốc xe vượt quá **T phút**.
* **Trạng thái:** `TBD`.
* **Câu hỏi BA cần làm rõ:** 
  > *Giới hạn M (số tài xế tối đa thử gán, ví dụ: 3 hay 5 tài xế) và thời gian timeout tổng T (ví dụ: 2 phút hay 3 phút) là bao nhiêu?*

---

### Nhóm 4: Quản lý Trạng thái Chuyến đi (BR-STATE)

#### `BR-STATE-01`: Tính đơn hướng của Vòng đời chuyến xe (FSM)
* **Mục tiêu:** Bảo toàn tính toàn vẹn dữ liệu vận hành và ngăn chặn sai lệch trạng thái.
* **Quy tắc:** Vòng đời chuyến xe tuân thủ nghiêm ngặt máy trạng thái hữu hạn (FSM) một chiều:
  $$\text{REQUESTED} \longrightarrow \text{MATCHED} \longrightarrow \text{PICKING\_UP} \longrightarrow \text{IN\_PROGRESS} \longrightarrow \text{COMPLETED}$$
  Tuyệt đối không cho phép nhảy cóc trạng thái hoặc quay ngược trạng thái trước đó.
* **Trạng thái:** `Confirmed`.

#### `BR-STATE-02`: Quyền cập nhật trạng thái thực tế
* **Mục tiêu:** Buộc tài xế chịu trách nhiệm về mốc thời gian và vị trí thực tế của hành trình.
* **Quy tắc:** 
  - Trạng thái `MATCHED`: Hệ thống tự động cập nhật khi Driver bấm "Chấp nhận".
  - Trạng thái `PICKING_UP`: Do Driver chủ động bấm khi đã lái xe đến điểm đón khách.
  - Trạng thái `IN_PROGRESS`: Do Driver chủ động bấm sau khi xác nhận khách đã lên xe an toàn.
  - Trạng thái `COMPLETED`: Do Driver chủ động bấm khi đã dừng xe tại điểm trả khách.
* **Trạng thái:** `Confirmed`.

---

### Nhóm 5: Tính cước & Thanh toán (BR-PRICING & BR-PAY)

#### `BR-PRICING-01`: Công thức cấu thành cước phí chuyến đi
* **Mục tiêu:** Đảm bảo công thức tính tiền minh bạch, tự động và đúng thỏa thuận kinh doanh.
* **Quy tắc:** Cước phí chuyến đi được tính toán tự động dựa trên bảng giá cấu hình theo loại xe:
  $$\text{Tổng cước} = \text{Giá mở cửa} + (\text{Quãng đường thực tế (km)} \times \text{Đơn giá/km}) + (\text{Thời gian di chuyển (phút)} \times \text{Đơn giá/phút})$$
* **Trạng thái:** `TBD`.
* **Câu hỏi BA cần làm rõ:** 
  > *Trong MVP có tính cước thời gian (theo phút) không hay chỉ tính theo số km thực tế? Bảng giá mở cửa và đơn giá từng km cho từng loại xe (4 chỗ, 7 chỗ, xe máy) cụ thể là bao nhiêu? Có quy định mức cước tối thiểu cho một chuyến đi không?*

#### `BR-PAY-01`: Xác nhận Thanh toán Tiền mặt (Cash)
* **Mục tiêu:** Thu hồi công nợ trực tiếp ngay tại thời điểm kết thúc hành trình.
* **Quy tắc:** Với phương thức Tiền mặt, Driver có nghĩa vụ thu tiền trực tiếp từ Customer đúng bằng số tiền chốt trên hóa đơn và bấm nút "Xác nhận đã nhận tiền" trên app để hoàn tất giao dịch tài chính của cuốc xe.
* **Trạng thái:** `Confirmed`.

#### `BR-PAY-02`: Xác thực Thanh toán Điện tử (Digital Payment)
* **Mục tiêu:** Đảm bảo giao dịch số được trừ tiền an toàn, chống gian lận tài chính.
* **Quy tắc:** Trạng thái thanh toán của cuốc xe chỉ được chuyển sang `PAID` khi hệ thống nhận được tín hiệu phản hồi xác nhận thành công (`Webhook/Callback`) có chữ ký điện tử hợp lệ từ Cổng thanh toán đối tác.
* **Trạng thái:** `Confirmed`.

#### `BR-PAY-03`: Xử lý Thanh toán Điện tử Thất bại
* **Mục tiêu:** Tránh giữ chân tài xế khi cổng trung gian gặp sự cố kết nối hoặc khách hết tiền thẻ.
* **Quy tắc:** Khi cổng thanh toán báo lỗi (thẻ hết hạn, không đủ số dư, timeout kết nối quá thời hạn quy định), hệ thống lập tức hiển thị cảnh báo cho cả Khách hàng và Tài xế, đồng thời tự động chuyển đổi phương thức thanh toán sang **Tiền mặt (Cash)** để tài xế thu trực tiếp tại chỗ.
* **Trạng thái:** `Confirmed`.

---

### Nhóm 6: Hủy chuyến & Phạt vi phạm (BR-CANCEL)

#### `BR-CANCEL-01`: Điều kiện Hủy chuyến và Phí hủy (Cancellation Fee)
* **Mục tiêu:** Ngăn chặn việc hủy chuyến tùy tiện gây thiệt hại chi phí xăng xe và thời gian của các bên.
* **Quy tắc:** 
  - Khách hàng được quyền hủy chuyến miễn phí khi hệ thống đang ở trạng thái `REQUESTED`.
  - Khách hàng hoặc tài xế có thể hủy chuyến khi ở trạng thái `MATCHED` hoặc `PICKING_UP` kèm theo việc bắt buộc chọn lý do hủy.
* **Trạng thái:** `TBD`.
* **Câu hỏi BA cần làm rõ:** 
  > *Nếu khách hàng hủy chuyến sau khi tài xế đã di chuyển đón quá 3 phút (hoặc tài xế đã đến nơi), khách hàng có bị phạt phí hủy chuyến không? Mức phí phạt là bao nhiêu và xử lý truy thu bằng cách nào trong phiên bản MVP?*

---

### Nhóm 7: Đánh giá & Giám sát Vận hành (BR-RATE & BR-OPS)

#### `BR-RATE-01`: Nguyên tắc Đánh giá Chất lượng
* **Mục tiêu:** Thu thập dữ liệu khách quan để đo lường mức độ hài lòng về dịch vụ.
* **Quy tắc:** Mỗi chuyến xe có trạng thái `COMPLETED` và thanh toán `PAID` chỉ được Customer đánh giá **duy nhất 01 lần**. Thang điểm đánh giá là số nguyên từ 1 đến 5 sao. Đánh giá khi đã gửi thành công sẽ được ghi nhận vĩnh viễn và không thể chỉnh sửa.
* **Trạng thái:** `Confirmed`.

#### `BR-OPS-01`: Quyền hạn Can thiệp của Vận hành (Operation Staff)
* **Mục tiêu:** Đảm bảo tính an toàn dữ liệu và quyền giải tỏa các điểm nghẽn của hệ thống.
* **Quy tắc:**




# ĐẶC TẢ YÊU CẦU NGHIỆP VỤ & HỆ THỐNG (SRS - MVP SCOPE)
## TẬP TRUNG 02 MODULE: QUẢN LÝ KHÁCH HÀNG & QUẢN LÝ TÀI XẾ

**Dự án:** Nền tảng đặt xe CAB System  
**Phiên bản:** MVP 1.0 (Giới hạn 2 phân hệ cốt lõi trong thời gian 7 tuần)  
**Vai trò:** Senior Business Analyst  
**Ngày cập nhật:** 06/09/2026  

---

## 1. MỤC TIÊU VÀ PHẠM VI GIỚI HẠN (SCOPE BOUNDARY)

Để đảm bảo dự án nghiệm thu khả thi và bàn giao đúng hạn trong 7 tuần, hệ thống đóng băng phạm vi ở hai phân hệ tiền đề quyết định việc vận hành:
1. **Module 1: Quản lý Khách hàng (Customer Management):** Quản lý định danh, trạng thái tài khoản, lịch sử đặt xe và tính hợp lệ khi gửi yêu cầu cuốc xe.
2. **Module 2: Quản lý Tài xế (Driver Management):** Quản lý hồ sơ đối tác, phương tiện vận tải, trạng thái sẵn sàng (Online/Offline/Busy), tọa độ GPS và kiểm duyệt điều kiện nhận cuốc.

---

## 2. MA TRẬN ÁNH XẠ BUSINESS RULES VÀO 2 MODULE (BR TRACEABILITY MATRIX)

| Mã BR | Tên quy tắc nghiệp vụ | Áp dụng vào Module | Trạng thái |
| :--- | :--- | :---: | :---: |
| **BR-AUTH-01** | Định danh duy nhất theo số điện thoại và phân quyền Role | Cả 2 Module | Confirmed |
| **BR-AUTH-02** | Điều kiện xác thực và kích hoạt tài xế hành nghề | Quản lý Tài xế | Confirmed |
| **BR-BOOKING-01** | Ràng buộc thông tin khởi tạo cuốc xe của khách hàng | Quản lý Khách hàng | Confirmed |
| **BR-BOOKING-02** | Giới hạn 01 cuốc xe hoạt động đồng thời trên mỗi khách | Quản lý Khách hàng | Confirmed |
| **BR-DRIVER-01** | 4 điều kiện cốt lõi để tài xế được nhận chuyến | Quản lý Tài xế | Confirmed |
| **BR-DRIVER-02** | Cơ chế cập nhật tọa độ GPS và xử lý ngắt kết nối | Quản lý Tài xế | TBD |
| **BR-RATE-01** | Tích lũy và cập nhật điểm đánh giá chất lượng phục vụ | Cả 2 Module | Confirmed |
| **BR-OPS-01** | Quyền hạn tra cứu, kích hoạt/khóa tài khoản của Vận hành | Cả 2 Module | Confirmed |

---

## 3. ĐẶC TẢ CHI TIẾT MODULE 1: QUẢN LÝ KHÁCH HÀNG (CUSTOMER MANAGEMENT)

### 3.1. Danh sách Chức năng (Functional Requirements)

| FR ID | Tên chức năng | Actor | Mô tả tóm tắt | Quy tắc liên quan | Mức ưu tiên |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **FR-CUS-01** | Đăng ký & Đăng nhập Khách hàng | Customer | Xác thực tài khoản qua SĐT và mật khẩu/mã OTP để cấp token truy cập. | `BR-AUTH-01` | **Must** |
| **FR-CUS-02** | Quản lý Thông tin Hồ sơ | Customer | Xem và cập nhật họ tên, email liên hệ, ảnh đại diện cơ bản. | `BR-AUTH-01` | **Should** |
| **FR-CUS-03** | Kiểm tra Tính hợp lệ khi Đặt xe | Customer, Hệ thống | Kiểm tra ràng buộc điều kiện không bị nợ cuốc hoặc đang kẹt cuốc xe khác. | `BR-BOOKING-01`<br>`BR-BOOKING-02` | **Must** |
| **FR-CUS-04** | Tra cứu Lịch sử Chuyến xe | Customer | Hiển thị danh sách cuốc xe đã đi kèm trạng thái, số tiền và thông tin tài xế. | `BR-RATE-01` | **Must** |
| **FR-CUS-05** | Quản trị Danh sách Khách hàng | Operation Staff | Tìm kiếm, xem chi tiết và khóa/mở khóa tài khoản khách hàng khi có gian lận. | `BR-OPS-01` | **Must** |

---

### 3.2. User Stories & Tiêu chí Nghiệm thu (Acceptance Criteria)

#### US-CUS-01: Kiểm tra ràng buộc trước khi gửi cuốc xe
* **User Story:** Là một **Hành khách (Customer)**, tôi muốn **hệ thống kiểm tra tính hợp lệ của tài khoản khi tôi bấm đặt xe**, để **tôi không bị xung đột cuốc xe hoặc tạo các yêu cầu ảo ngoài ý muốn.**
* **Acceptance Criteria (AC):**
  * `AC-01.1:` Nếu khách hàng đang có 01 cuốc xe ở các trạng thái `REQUESTED`, `MATCHED`, `PICKING_UP`, `IN_PROGRESS`, hệ thống chặn không cho tạo cuốc mới và hiển thị thông báo: *"Bạn đang có chuyến xe chưa hoàn thành. Vui lòng kiểm tra lại hành trình hiện tại."* (Theo `BR-BOOKING-02`).
  * `AC-01.2:` Khách hàng bắt buộc phải nhập đủ tọa độ điểm đón và điểm trả với khoảng cách tối thiểu từ 100m trở lên trước khi gửi yêu cầu (Theo `BR-BOOKING-01`).
* **Priority:** Must Have.

#### US-CUS-02: Giám sát tài khoản khách hàng từ phía Vận hành
* **User Story:** Là một **Nhân viên Vận hành (Operation Staff)**, tôi muốn **tra cứu hồ sơ khách hàng theo SĐT và có quyền tạm khóa tài khoản**, để **xử lý các trường hợp tài khoản spam hoặc vi phạm quy chế an toàn.**
* **Acceptance Criteria (AC):**
  * `AC-02.1:` Cho phép tìm kiếm chính xác khách hàng qua Số điện thoại hoặc Mã khách hàng (`Customer_ID`).
  * `AC-02.2:` Hiển thị đầy đủ: Ngày tạo, Tổng số chuyến đã đặt, Tỷ lệ hủy chuyến, Trạng thái tài khoản (`ACTIVE`, `SUSPENDED`).
  * `AC-02.3:` Nhân viên có quyền bấm "Khóa tài khoản" kèm ô nhập lý do bắt buộc (tối thiểu 10 ký tự). Tài khoản bị khóa sẽ bị đăng xuất ngay lập tức.
* **Priority:** Must Have.

---

### 3.3. Cấu trúc Dữ liệu Khách hàng (Data Schema)
  - Operation Staff có quyền tra cứu thông tin chi tiết toàn bộ lịch sử các cuốc xe.
  - Operation Staff được quyền thực hiện lệnh **Hủy cuốc cưỡng bức (Force Cancel)** kèm nhập lý do nghiệp vụ bắt buộc đối với các chuyến xe đang treo (`REQUESTED`, `MATCHED`, `PICKING_UP`, `IN_PROGRESS`).
  - Operation Staff **không được phép** chỉnh sửa số tiền cước của những chuyến đi đã chuyển trạng thái `PAID`.
* **Trạng thái:** `Confirmed`.


### BR-VEHICLE-SEL-01: Danh mục loại xe hỗ trợ trong MVP
* **Mã quy tắc:** `BR-VEHICLE-SEL-01`
* **Tên quy tắc:** Giới hạn phân loại phương tiện trong giai đoạn MVP.
* **Mục tiêu doanh nghiệp:** Giảm tải độ phức tạp vận hành và tập trung vào phân khúc phương tiện phổ biến nhất để kiểm chứng thị trường.
* **Nội dung quy tắc:**
  - Hệ thống chỉ cung cấp hiển thị và hỗ trợ đặt đúng **02 phân loại phương tiện**:
    1. `MOTORBIKE` (Xe máy 2 bánh - chở tối đa 01 khách).
    2. `CAR_4_SEATS` (Ô tô 4 chỗ tiêu chuẩn - chở tối đa 04 khách).
  - Các dòng xe khác (`CAR_7_SEATS`, xe cao cấp `PREMIUM`, xe giao hàng `DELIVERY`) hoàn toàn **Out-of-Scope** ở bản MVP 1.0.
* **Trạng thái:** `Confirmed`.

---

### BR-VEHICLE-SEL-02: Ràng buộc tính cước và hiển thị theo loại xe
* **Mã quy tắc:** `BR-VEHICLE-SEL-02`
* **Tên quy tắc:** Hiển thị giá cước ước tính theo từng loại xe.
* **Mục tiêu doanh nghiệp:** Minh bạch chi phí, giúp khách hàng tự cân đối nhu cầu và khả năng chi trả, hạn chế hủy chuyến do hiểu nhầm giá.
* **Nội dung quy tắc:**
  - Khi khách hàng đã nhập đủ điểm đón và điểm trả hợp lệ:
    - Hệ thống bắt buộc tính toán đồng thời và hiển thị giá ước tính (`Estimated_Fare`) cho cả 2 loại xe (`MOTORBIKE` và `CAR_4_SEATS`) trên cùng một màn hình lựa chọn.
    - Công thức ước tính áp dụng đơn giá riêng biệt theo cấu hình của từng loại xe:
      $$\text{Estimated\_Fare}_{\text{type}} = \text{Base\_Fare}_{\text{type}} + (\text{Estimated\_Distance} \times \text{Rate\_Per\_Km}_{\text{type}})$$
  - Giá hiển thị phải được làm tròn đến hàng nghìn đồng (VND).
* **Trạng thái:** `Confirmed`.

---

### BR-VEHICLE-SEL-03: Ràng buộc loại xe khi khởi tạo yêu cầu đặt xe
* **Mã quy tắc:** `BR-VEHICLE-SEL-03`
* **Tên quy tắc:** Chọn loại xe bắt buộc khi gửi Booking.
* **Mục tiêu doanh nghiệp:** Tránh tạo các cuốc xe không xác định phương tiện, đảm bảo thuật toán điều phối gán đúng tài xế sở hữu loại xe phù hợp.
* **Nội dung quy tắc:**
  - Khách hàng bắt buộc phải chọn duy nhất **01 loại xe** tại một thời điểm đặt chuyến.
  - Loại xe được chọn mặc định ban đầu (`Default Selection`) là loại xe mà khách hàng đã đặt ở chuyến đi thành công gần nhất (nếu là khách mới: mặc định chọn `MOTORBIKE`).
  - Nút "Xác nhận đặt xe" chỉ kích hoạt (enable) khi đã có 01 loại xe được chọn.
  - Khi yêu cầu được gửi đi, mã loại xe đã chọn (`Vehicle_Type`) sẽ được gắn cố định vào bản ghi `Booking` và **không được phép thay đổi** trong suốt vòng đời cuốc xe.
* **Trạng thái:** `Confirmed`.

---

### BR-VEHICLE-SEL-04: Cảnh báo nguồn cung phương tiện khả dụng (Availability Check)
* **Mã quy tắc:** `BR-VEHICLE-SEL-04`
* **Tên quy tắc:** Kiểm tra sơ bộ số lượng tài xế theo loại xe tại khu vực đón.
* **Mục tiêu doanh nghiệp:** Quản trị kỳ vọng của khách hàng, tránh để khách đặt cuốc ở những vùng không có sẵn xe loại đó.
* **Nội dung quy tắc:**
  - Khi khách hàng chọn một loại xe, hệ thống đếm nhanh số lượng tài xế thỏa mãn điều kiện `BR-DRIVER-01` sở hữu đúng loại xe đó trong bán kính quy định (ví dụ: 3km).
  - Nếu số tài xế khả dụng = 0: 
    - Cho phép khách đặt tiếp nhưng hiển thị nhãn cảnh báo: *"Khu vực này hiện đang có ít tài xế [Loại xe], thời gian tìm xe có thể lâu hơn dự kiến."*
* **Trạng thái:** `TBD`.
* **Câu hỏi BA cần làm rõ:** 
  > *Trong bản MVP 7 tuần, có cần hiển thị cảnh báo này ngay trên màn hình chọn xe không, hay cứ cho phép khách bấm đặt xe rồi để thuật toán tự quét và trả về `NO_DRIVER_FOUND` nếu hết xe?*
  

# Business Requirements – CAB System

## 1. Mục tiêu nghiệp vụ

Dựa trên yêu cầu của khách hàng, CAB System hướng đến việc xây dựng một nền tảng đặt xe trực tuyến có khả năng hỗ trợ đầy đủ quy trình từ khi khách hàng tạo yêu cầu đặt xe, hệ thống tìm tài xế, tài xế thực hiện chuyến đi, hệ thống tính cước, thanh toán cho đến khi khách hàng đánh giá tài xế.

Các Business Requirement chính được xác định như sau:

| Mã | Business Requirement |
|---|---|
| **BR-01** | Tự động hóa quy trình đặt xe và phân công tài xế nhằm giảm sự phụ thuộc vào việc điều phối thủ công. |
| **BR-02** | Cho phép khách hàng tạo yêu cầu đặt xe và theo dõi trạng thái chuyến đi trong suốt quá trình sử dụng dịch vụ. |
| **BR-03** | Tự động tìm và phân công tài xế phù hợp dựa trên vị trí, trạng thái sẵn sàng và các tiêu chí vận hành khác. |
| **BR-04** | Quản lý toàn bộ vòng đời chuyến đi từ khi tạo yêu cầu, tìm tài xế, thực hiện chuyến đến khi hoàn thành. |
| **BR-05** | Hỗ trợ tính cước và quản lý thanh toán tập trung, bao gồm thanh toán bằng tiền mặt và thanh toán điện tử. |
| **BR-06** | Cung cấp thông báo kịp thời cho khách hàng và tài xế tại các sự kiện quan trọng của chuyến đi. |
| **BR-07** | Hỗ trợ nhân viên vận hành theo dõi tài xế, chuyến đi, giao dịch và hỗ trợ xử lý các trường hợp phát sinh. |
| **BR-08** | Đảm bảo xác thực người dùng, phân quyền truy cập, bảo vệ dữ liệu và lưu vết các thao tác quan trọng. |
| **BR-09** | Đảm bảo hệ thống hoạt động ổn định khi nhu cầu tăng cao và hạn chế việc lỗi của một thành phần làm gián đoạn toàn bộ hệ thống. |
| **BR-10** | Xây dựng nền tảng có kiến trúc linh hoạt, cho phép mở rộng thêm loại dịch vụ, phương thức thanh toán, nhà cung cấp thông báo và các chức năng mới trong tương lai. |

## 2. Mối liên hệ với MVP

Trong phạm vi MVP 7 tuần, các Business Requirement được ưu tiên theo hướng đảm bảo hệ thống có thể vận hành end-to-end:

**Khách hàng tạo yêu cầu → Hệ thống tìm tài xế → Tài xế nhận chuyến → Thực hiện chuyến → Hoàn thành → Tính cước → Thanh toán → Đánh giá.**

Các yêu cầu như báo cáo quản trị nâng cao, nhiều nhà cung cấp thanh toán, nhiều kênh thông báo hoặc phân tích hiệu suất tài xế chuyên sâu chưa phải trọng tâm của MVP và có thể được triển khai ở các phase sau.

## 3. Lưu ý

- **BR** trong tài liệu này được dùng để chỉ **Business Requirement**.
- Các quy tắc nghiệp vụ chi tiết nên sử dụng mã riêng, ví dụ **BRU-01, BRU-02...**, để tránh nhầm với Business Requirement.
- Các nội dung khách hàng chưa xác định rõ như cách tính cước, tiêu chí ưu tiên tài xế, thời gian phản hồi, chính sách hủy chuyến, xử lý mất kết nối và thời gian lưu trữ dữ liệu cần được đánh dấu **TBD** và xác nhận lại với khách hàng.







