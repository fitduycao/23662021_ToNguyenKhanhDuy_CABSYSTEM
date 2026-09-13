# CAB — Bộ API theo 8 module MVP

**Chỉ cần đưa thư mục này lên GitHub: 8 file YAML + file README này.** Mỗi YAML mở độc lập trong Swagger Editor bằng **File → Import File**. Không cần `common/`, file đầu mối hoặc các thư mục trong bộ cũ.

## Bố cục để báo cáo

| MVP | File | Nội dung trình bày | Số API |
|---|---|---|---|
| MVP-01 | [01-tai-khoan.yaml](01-tai-khoan.yaml) | Tài khoản và phân quyền | 15 |
| MVP-02 | [02-tai-xe-phuong-tien.yaml](02-tai-xe-phuong-tien.yaml) | Tài xế và phương tiện | 14 |
| MVP-03 | [03-dat-xe-dieu-phoi.yaml](03-dat-xe-dieu-phoi.yaml) | Đặt xe và điều phối | 6 |
| MVP-04 | [04-theo-doi-chuyen.yaml](04-theo-doi-chuyen.yaml) | Thực hiện và theo dõi chuyến | 4 |
| MVP-05 | [05-cuoc-thanh-toan.yaml](05-cuoc-thanh-toan.yaml) | Cước và thanh toán | 6 |
| MVP-06 | [06-thong-bao.yaml](06-thong-bao.yaml) | Thông báo | 2 |
| MVP-07 | [07-lich-su-danh-gia.yaml](07-lich-su-danh-gia.yaml) | Lịch sử và đánh giá | 3 |
| MVP-08 | [08-van-hanh-bao-cao.yaml](08-van-hanh-bao-cao.yaml) | Vận hành và báo cáo | 9 |

Tổng cộng 59 operation được giữ từ bản trước, chỉ tổ chức lại theo 8 MVP, không phải 59 chức năng bắt buộc phải trình diễn. Tên function nằm ở `operationId`; mã yêu cầu nằm ở `x-functional-requirements`. Các module này là nhóm chức năng, không có nghĩa phải triển khai 8 microservice.

## Cách trình bày ngắn gọn

1. **Giới thiệu:** “Em chia API thành 8 module theo MVP trong SRS, bao phủ quy trình từ đăng ký, đặt xe, nhận chuyến đến thanh toán và đánh giá.”
2. **Trình bày CRUD ở MVP-01:** `POST /users` tạo khách hàng bởi vận hành; `GET /users` lấy danh sách; `GET /users/{userId}` lấy chi tiết; `PATCH /users/{userId}` cập nhật; `DELETE /users/{userId}` xóa mềm. Khách tự đăng ký dùng `/auth/register`.
3. **Trình bày luồng chính:** MVP-03 tạo chuyến và tài xế nhận → MVP-04 cập nhật chuyến → MVP-05 lấy cước và thanh toán → MVP-07 xem lịch sử, đánh giá. MVP-02 cung cấp tài xế/xe, MVP-06 thông báo và MVP-08 hỗ trợ vận hành.
4. **Với mỗi API được chọn:** nêu chức năng, method/endpoint, ai có quyền, request mẫu, response thành công và một lỗi tiêu biểu. Không cần đọc hết từng dòng YAML.
5. **Kết luận phạm vi:** đây là đặc tả API. Cước, hủy chuyến, thời gian ghép xe và quyền chi tiết còn TBD theo yêu cầu khách hàng; chưa phải backend hoạt động.

## Các điểm cần giải thích khi được hỏi

- Xóa user/driver/vehicle là xóa mềm để giữ lịch sử; thao tác này được đánh dấu đề xuất mở rộng, chưa phải chính sách đã được khách hàng phê duyệt.
- Tìm tài xế, tìm tiếp khi từ chối/hết hạn, tính cước sau hoàn thành, gửi thông báo và ghi audit là xử lý nền được kích hoạt từ nghiệp vụ. Không cho người dùng gọi API tùy ý tự phân công hoặc tự nhập cước.
- `GET /trips` đặt ở MVP-07 vì dùng cho lịch sử; vận hành cũng có thể dùng theo quyền để xem chuyến. Một endpoint có thể phục vụ nhiều màn hình, chỉ khai báo một lần.
- MVP-05 có webhook riêng cho đối tác, xác thực bằng chữ ký; khách hàng không được tự gửi kết quả thanh toán.
- Các định dạng dữ liệu, vai trò, thang điểm và xử lý hỗ trợ trong API là đề xuất phân tích, cần xác nhận các TBD ghi trong SRS.
- Swagger hiển thị DELETE bằng màu đỏ. Response thành công là 204 không có body. Mỗi file mới dùng tham chiếu nội bộ `#/components/...`, tránh lỗi tải file ngoài khi nhập riêng.

## Truy vết từng API

| MVP | Method và endpoint | Function | FR |
|---|---|---|---|
| MVP-01 | `GET /roles` | `listRoles` | FR-24 |
| MVP-01 | `GET /permissions` | `listPermissions` | FR-24 |
| MVP-01 | `GET /users/{userId}/roles` | `getUserRoles` | FR-24 |
| MVP-01 | `PUT /users/{userId}/roles` | `assignUserRoles` | FR-24, FR-26 |
| MVP-01 | `POST /auth/register` | `registerCustomer` | FR-01 |
| MVP-01 | `POST /auth/drivers/register` | `registerDriver` | FR-02 |
| MVP-01 | `POST /auth/login` | `login` | FR-01, FR-02 |
| MVP-01 | `POST /users` | `createUser` | FR-20 |
| MVP-01 | `GET /users` | `listUsers` | FR-20 |
| MVP-01 | `GET /users/me` | `getMyProfile` | FR-01, FR-02 |
| MVP-01 | `PATCH /users/me` | `updateMyProfile` | FR-01, FR-02 |
| MVP-01 | `GET /users/{userId}` | `getUserById` | FR-20 |
| MVP-01 | `PATCH /users/{userId}` | `updateUser` | FR-20 |
| MVP-01 | `DELETE /users/{userId}` | `deleteUser` | FR-20 |
| MVP-01 | `PATCH /users/{userId}/status` | `changeUserStatus` | FR-20, FR-24 |
| MVP-02 | `POST /drivers` | `createDriver` | FR-02, FR-20 |
| MVP-02 | `GET /drivers` | `listDrivers` | FR-20, FR-21 |
| MVP-02 | `GET /drivers/{driverId}` | `getDriverById` | FR-02, FR-21 |
| MVP-02 | `PATCH /drivers/{driverId}` | `updateDriver` | FR-02, FR-20 |
| MVP-02 | `DELETE /drivers/{driverId}` | `deactivateDriver` | FR-20 |
| MVP-02 | `PATCH /drivers/{driverId}/availability` | `updateDriverAvailability` | FR-04 |
| MVP-02 | `PUT /drivers/{driverId}/location` | `updateDriverLocation` | FR-04 |
| MVP-02 | `GET /drivers/{driverId}/location` | `getDriverLocation` | FR-04, FR-21 |
| MVP-02 | `GET /service-types` | `listServiceTypes` | FR-05 |
| MVP-02 | `POST /vehicles` | `createVehicle` | FR-03, FR-20 |
| MVP-02 | `GET /vehicles` | `listVehicles` | FR-03, FR-20 |
| MVP-02 | `GET /vehicles/{vehicleId}` | `getVehicleById` | FR-03, FR-20 |
| MVP-02 | `PATCH /vehicles/{vehicleId}` | `updateVehicle` | FR-03, FR-20 |
| MVP-02 | `DELETE /vehicles/{vehicleId}` | `deactivateVehicle` | FR-20 |
| MVP-03 | `GET /dispatch-offers` | `listMyDispatchOffers` | FR-07, FR-19 |
| MVP-03 | `GET /dispatch-offers/{offerId}` | `getDispatchOffer` | FR-07 |
| MVP-03 | `POST /dispatch-offers/{offerId}/accept` | `acceptDispatchOffer` | FR-07, FR-09, FR-18 |
| MVP-03 | `POST /dispatch-offers/{offerId}/decline` | `declineDispatchOffer` | FR-07, FR-08 |
| MVP-03 | `POST /trips` | `createTrip` | FR-05, FR-06, FR-08, FR-18 |
| MVP-03 | `POST /trips/{tripId}/cancellations` | `cancelTrip` | FR-27, FR-19 |
| MVP-04 | `GET /trips/{tripId}` | `getTripById` | FR-09, FR-11, FR-21 |
| MVP-04 | `GET /trips/{tripId}/tracking` | `trackTrip` | FR-09 |
| MVP-04 | `PATCH /trips/{tripId}/status` | `updateTripStatus` | FR-10, FR-13, FR-18, FR-19 |
| MVP-04 | `GET /trips/{tripId}/status-history` | `listTripStatusHistory` | FR-10, FR-21 |
| MVP-05 | `GET /trips/{tripId}/fare` | `getTripFare` | FR-11, FR-13 |
| MVP-05 | `POST /trips/{tripId}/payments` | `createTripPayment` | FR-14, FR-15, FR-17 |
| MVP-05 | `GET /trips/{tripId}/payments` | `listTripPayments` | FR-11, FR-17, FR-23 |
| MVP-05 | `GET /payments/{paymentId}` | `getPaymentById` | FR-16, FR-17, FR-23 |
| MVP-05 | `POST /payments/{paymentId}/cash-confirmation` | `confirmCashPayment` | FR-14 |
| MVP-05 | `POST /payments/provider-webhook` | `handlePaymentWebhook` | FR-16, FR-18 |
| MVP-06 | `GET /notifications` | `listMyNotifications` | FR-18, FR-19 |
| MVP-06 | `GET /notifications/{notificationId}` | `getNotificationById` | FR-18, FR-19 |
| MVP-07 | `POST /trips/{tripId}/ratings` | `createTripRating` | FR-12 |
| MVP-07 | `GET /trips/{tripId}/ratings` | `listTripRatings` | FR-12 |
| MVP-07 | `GET /trips` | `listTrips` | FR-11, FR-21 |
| MVP-08 | `GET /audit-logs` | `listAuditLogs` | FR-26 |
| MVP-08 | `GET /audit-logs/{auditId}` | `getAuditLogById` | FR-26 |
| MVP-08 | `GET /operations/transactions` | `listTransactions` | FR-23 |
| MVP-08 | `POST /operations/support-cases` | `createSupportCase` | FR-22 |
| MVP-08 | `GET /operations/support-cases` | `listSupportCases` | FR-22 |
| MVP-08 | `GET /operations/support-cases/{caseId}` | `getSupportCaseById` | FR-22 |
| MVP-08 | `POST /operations/support-cases/{caseId}/resolution` | `resolveSupportCase` | FR-22, FR-26 |
| MVP-08 | `GET /reports/summary` | `getOperationalSummary` | FR-25 |
| MVP-08 | `GET /reports/driver-performance` | `listDriverPerformance` | FR-25 |

Nguồn: SRS 16 mục đã phân tích từ Customer-Requirement.docx. Quy cách tham chiếu nội bộ: https://swagger.io/docs/specification/v3_0/using-ref/
