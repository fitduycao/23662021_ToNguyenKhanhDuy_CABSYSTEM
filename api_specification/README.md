# CAB — 10 nhóm API

Bộ này gồm **10 file YAML**, đặt tên theo mẫu bạn cung cấp. Mỗi nhóm chứa nhiều endpoint, tổng cộng 59 operation; “10 nhóm API” không có nghĩa chỉ 10 endpoint. Mỗi file mở độc lập bằng **Swagger Editor → File → Import File**, không cần common/ hoặc file đầu mối.

| File | Nhóm chức năng | Số endpoint/operation |
|---|---|---|
| [1_auth_api.yaml](1_auth_api.yaml) | Xác thực | 3 |
| [2_customer_profile_api.yaml](2_customer_profile_api.yaml) | Hồ sơ khách hàng | 2 |
| [3_driver_profile_api.yaml](3_driver_profile_api.yaml) | Hồ sơ tài xế và phương tiện | 8 |
| [4_booking_api.yaml](4_booking_api.yaml) | Đặt xe và nhận chuyến | 7 |
| [5_location_api.yaml](5_location_api.yaml) | Vị trí và theo dõi | 3 |
| [6_trip_execution_api.yaml](6_trip_execution_api.yaml) | Thực hiện chuyến | 3 |
| [7_payment_api.yaml](7_payment_api.yaml) | Cước và thanh toán | 6 |
| [8_rating_history_api.yaml](8_rating_history_api.yaml) | Đánh giá và lịch sử | 3 |
| [9_admin_users_api.yaml](9_admin_users_api.yaml) | Quản trị người dùng | 13 |
| [10_admin_operations_api.yaml](10_admin_operations_api.yaml) | Vận hành và báo cáo | 11 |

## Cách trả lời khi báo cáo

- **API xác thực ở đâu?** File 1: đăng ký khách, đăng ký tài xế theo phạm vi mở rộng, đăng nhập.
- **API User ở đâu?** File 2 là người dùng xem/sửa hồ sơ của mình; file 9 là CRUD và quản lý user bởi vận hành/quản trị.
- **API Driver ở đâu?** File 3 là hồ sơ, phương tiện và trạng thái tài xế; file 9 có vận hành tạo và tra cứu tài xế.
- **API thanh toán ở đâu?** File 7: lấy cước, tạo lần thanh toán, xem kết quả, xác nhận tiền mặt và nhận webhook có chữ ký.
- **Tên function ở đâu?** Xem operationId hoặc x-function, ví dụ login, createUser, updateDriver, createTripPayment.
- File 10 chứa vận hành, báo cáo, audit và đọc thông báo. Không phải mọi endpoint trong file đều dành cho admin: thông báo vẫn chỉ cho chủ tài khoản, theo security và mô tả quyền.

## Quan hệ với kế hoạch 7 tuần

SRS 2.0 vừa thu gọn chỉ có quản lý khách hàng và quản lý tài xế. Bộ 10 nhóm này có thêm API theo tầm nhìn CAB đầy đủ do bạn yêu cầu bổ sung xác thực, thanh toán và các nhóm như ảnh. **Không tuyên bố triển khai toàn bộ 59 operation trong 7 tuần.**
Các mã FR-01–FR-27 và TBD trong YAML giữ nghĩa của bản phân tích CAB đầy đủ trước đó, không phải FR-MVP trong SRS 2.0. Muốn đưa nhóm đặt xe/thanh toán vào MVP thực hiện phải cập nhật phạm vi, truy vết và kế hoạch SRS trước. Bộ này không tự thay đổi SRS 2.0.
Các đề xuất như xóa mềm, một đánh giá/chuyến, thang điểm, thời hạn và phân quyền chi tiết chưa phải quyết định của khách hàng. Không có backend thật tại URL example.com.

## Danh sách function để tra cứu

| File | Method và endpoint | Function |
|---|---|---|
| 1 | `POST /auth/register` | `registerCustomer` |
| 1 | `POST /auth/drivers/register` | `registerDriver` |
| 1 | `POST /auth/login` | `login` |
| 2 | `GET /users/me` | `getMyProfile` |
| 2 | `PATCH /users/me` | `updateMyProfile` |
| 3 | `GET /drivers/{driverId}` | `getDriverById` |
| 3 | `PATCH /drivers/{driverId}` | `updateDriver` |
| 3 | `PATCH /drivers/{driverId}/availability` | `updateDriverAvailability` |
| 3 | `POST /vehicles` | `createVehicle` |
| 3 | `GET /vehicles` | `listVehicles` |
| 3 | `GET /vehicles/{vehicleId}` | `getVehicleById` |
| 3 | `PATCH /vehicles/{vehicleId}` | `updateVehicle` |
| 3 | `DELETE /vehicles/{vehicleId}` | `deactivateVehicle` |
| 4 | `GET /dispatch-offers` | `listMyDispatchOffers` |
| 4 | `GET /dispatch-offers/{offerId}` | `getDispatchOffer` |
| 4 | `POST /dispatch-offers/{offerId}/accept` | `acceptDispatchOffer` |
| 4 | `POST /dispatch-offers/{offerId}/decline` | `declineDispatchOffer` |
| 4 | `GET /service-types` | `listServiceTypes` |
| 4 | `POST /trips` | `createTrip` |
| 4 | `POST /trips/{tripId}/cancellations` | `cancelTrip` |
| 5 | `PUT /drivers/{driverId}/location` | `updateDriverLocation` |
| 5 | `GET /drivers/{driverId}/location` | `getDriverLocation` |
| 5 | `GET /trips/{tripId}/tracking` | `trackTrip` |
| 6 | `GET /trips/{tripId}` | `getTripById` |
| 6 | `PATCH /trips/{tripId}/status` | `updateTripStatus` |
| 6 | `GET /trips/{tripId}/status-history` | `listTripStatusHistory` |
| 7 | `GET /trips/{tripId}/fare` | `getTripFare` |
| 7 | `POST /trips/{tripId}/payments` | `createTripPayment` |
| 7 | `GET /trips/{tripId}/payments` | `listTripPayments` |
| 7 | `GET /payments/{paymentId}` | `getPaymentById` |
| 7 | `POST /payments/{paymentId}/cash-confirmation` | `confirmCashPayment` |
| 7 | `POST /payments/provider-webhook` | `handlePaymentWebhook` |
| 8 | `POST /trips/{tripId}/ratings` | `createTripRating` |
| 8 | `GET /trips/{tripId}/ratings` | `listTripRatings` |
| 8 | `GET /trips` | `listTrips` |
| 9 | `GET /roles` | `listRoles` |
| 9 | `GET /permissions` | `listPermissions` |
| 9 | `GET /users/{userId}/roles` | `getUserRoles` |
| 9 | `PUT /users/{userId}/roles` | `assignUserRoles` |
| 9 | `POST /drivers` | `createDriver` |
| 9 | `GET /drivers` | `listDrivers` |
| 9 | `DELETE /drivers/{driverId}` | `deactivateDriver` |
| 9 | `POST /users` | `createUser` |
| 9 | `GET /users` | `listUsers` |
| 9 | `GET /users/{userId}` | `getUserById` |
| 9 | `PATCH /users/{userId}` | `updateUser` |
| 9 | `DELETE /users/{userId}` | `deleteUser` |
| 9 | `PATCH /users/{userId}/status` | `changeUserStatus` |
| 10 | `GET /audit-logs` | `listAuditLogs` |
| 10 | `GET /audit-logs/{auditId}` | `getAuditLogById` |
| 10 | `GET /notifications` | `listMyNotifications` |
| 10 | `GET /notifications/{notificationId}` | `getNotificationById` |
| 10 | `GET /operations/transactions` | `listTransactions` |
| 10 | `POST /operations/support-cases` | `createSupportCase` |
| 10 | `GET /operations/support-cases` | `listSupportCases` |
| 10 | `GET /operations/support-cases/{caseId}` | `getSupportCaseById` |
| 10 | `POST /operations/support-cases/{caseId}/resolution` | `resolveSupportCase` |
| 10 | `GET /reports/summary` | `getOperationalSummary` |
| 10 | `GET /reports/driver-performance` | `listDriverPerformance` |
