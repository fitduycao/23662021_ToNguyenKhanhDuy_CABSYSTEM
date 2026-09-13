# Danh mục API và function

Các endpoint bên dưới nối sau `/api/v1`. Quyền và TBD xem trong file module tương ứng.

| Module | Method | Endpoint | Function | Chức năng | FR |
|---|---|---|---|---|---|
| [auth](auth/api.yaml) | POST | `/auth/register` | `registerCustomer` | Đăng ký tài khoản khách hàng | FR-01 |
| [auth](auth/api.yaml) | POST | `/auth/drivers/register` | `registerDriver` | Tài xế tự đăng ký | FR-02 |
| [auth](auth/api.yaml) | POST | `/auth/login` | `login` | Đăng nhập | FR-01, FR-02 |
| [users](users/api.yaml) | POST | `/users` | `createUser` | Tạo mới một user khách hàng | FR-20 |
| [users](users/api.yaml) | GET | `/users` | `listUsers` | Lấy danh sách user khách hàng | FR-20 |
| [users](users/api.yaml) | GET | `/users/me` | `getMyProfile` | Lấy hồ sơ tài khoản đang đăng nhập | FR-01, FR-02 |
| [users](users/api.yaml) | PATCH | `/users/me` | `updateMyProfile` | Cập nhật hồ sơ của chính mình | FR-01, FR-02 |
| [users](users/api.yaml) | GET | `/users/{userId}` | `getUserById` | Lấy chi tiết một user | FR-20 |
| [users](users/api.yaml) | PATCH | `/users/{userId}` | `updateUser` | Cập nhật thông tin một user | FR-20 |
| [users](users/api.yaml) | DELETE | `/users/{userId}` | `deleteUser` | Xóa mềm user (vô hiệu hóa tài khoản) | FR-20 |
| [users](users/api.yaml) | PATCH | `/users/{userId}/status` | `changeUserStatus` | Thay đổi trạng thái tài khoản | FR-20, FR-24 |
| [drivers](drivers/api.yaml) | POST | `/drivers` | `createDriver` | Vận hành tạo tài khoản tài xế | FR-02, FR-20 |
| [drivers](drivers/api.yaml) | GET | `/drivers` | `listDrivers` | Lấy danh sách tài xế | FR-20, FR-21 |
| [drivers](drivers/api.yaml) | GET | `/drivers/{driverId}` | `getDriverById` | Lấy chi tiết tài xế | FR-02, FR-21 |
| [drivers](drivers/api.yaml) | PATCH | `/drivers/{driverId}` | `updateDriver` | Cập nhật hồ sơ tài xế | FR-02, FR-20 |
| [drivers](drivers/api.yaml) | DELETE | `/drivers/{driverId}` | `deactivateDriver` | Xóa mềm tài xế | FR-20 |
| [drivers](drivers/api.yaml) | PATCH | `/drivers/{driverId}/availability` | `updateDriverAvailability` | Đổi trạng thái sẵn sàng của tài xế | FR-04 |
| [drivers](drivers/api.yaml) | PUT | `/drivers/{driverId}/location` | `updateDriverLocation` | Gửi vị trí mới của tài xế | FR-04 |
| [drivers](drivers/api.yaml) | GET | `/drivers/{driverId}/location` | `getDriverLocation` | Lấy vị trí hiện có của tài xế | FR-04, FR-21 |
| [vehicles](vehicles/api.yaml) | POST | `/vehicles` | `createVehicle` | Tạo mới phương tiện | FR-03, FR-20 |
| [vehicles](vehicles/api.yaml) | GET | `/vehicles` | `listVehicles` | Lấy danh sách phương tiện | FR-03, FR-20 |
| [vehicles](vehicles/api.yaml) | GET | `/vehicles/{vehicleId}` | `getVehicleById` | Lấy chi tiết phương tiện | FR-03, FR-20 |
| [vehicles](vehicles/api.yaml) | PATCH | `/vehicles/{vehicleId}` | `updateVehicle` | Cập nhật phương tiện | FR-03, FR-20 |
| [vehicles](vehicles/api.yaml) | DELETE | `/vehicles/{vehicleId}` | `deactivateVehicle` | Xóa mềm phương tiện | FR-20 |
| [service-types](service-types/api.yaml) | GET | `/service-types` | `listServiceTypes` | Lấy danh sách loại xe/dịch vụ | FR-05 |
| [trips](trips/api.yaml) | POST | `/trips` | `createTrip` | Tạo mới yêu cầu đặt xe | FR-05, FR-06, FR-08, FR-18 |
| [trips](trips/api.yaml) | GET | `/trips` | `listTrips` | Lấy danh sách/lịch sử chuyến đi | FR-11, FR-21 |
| [trips](trips/api.yaml) | GET | `/trips/{tripId}` | `getTripById` | Lấy chi tiết một chuyến đi | FR-09, FR-11, FR-21 |
| [trips](trips/api.yaml) | GET | `/trips/{tripId}/tracking` | `trackTrip` | Theo dõi tài xế, ETA và trạng thái chuyến | FR-09 |
| [trips](trips/api.yaml) | PATCH | `/trips/{tripId}/status` | `updateTripStatus` | Cập nhật quá trình thực hiện chuyến | FR-10, FR-13, FR-18, FR-19 |
| [trips](trips/api.yaml) | GET | `/trips/{tripId}/status-history` | `listTripStatusHistory` | Lấy lịch sử trạng thái chuyến | FR-10, FR-21 |
| [trips](trips/api.yaml) | POST | `/trips/{tripId}/cancellations` | `cancelTrip` | Hủy chuyến theo chính sách | FR-27, FR-19 |
| [dispatch](dispatch/api.yaml) | GET | `/dispatch-offers` | `listMyDispatchOffers` | Lấy danh sách đề nghị nhận chuyến | FR-07, FR-19 |
| [dispatch](dispatch/api.yaml) | GET | `/dispatch-offers/{offerId}` | `getDispatchOffer` | Lấy chi tiết đề nghị nhận chuyến | FR-07 |
| [dispatch](dispatch/api.yaml) | POST | `/dispatch-offers/{offerId}/accept` | `acceptDispatchOffer` | Chấp nhận chuyến | FR-07, FR-09, FR-18 |
| [dispatch](dispatch/api.yaml) | POST | `/dispatch-offers/{offerId}/decline` | `declineDispatchOffer` | Từ chối chuyến | FR-07, FR-08 |
| [fares](fares/api.yaml) | GET | `/trips/{tripId}/fare` | `getTripFare` | Lấy cước của chuyến đi | FR-11, FR-13 |
| [payments](payments/api.yaml) | POST | `/trips/{tripId}/payments` | `createTripPayment` | Tạo thanh toán hoặc thử lại sau thất bại | FR-14, FR-15, FR-17 |
| [payments](payments/api.yaml) | GET | `/trips/{tripId}/payments` | `listTripPayments` | Lấy các lần thanh toán của chuyến | FR-11, FR-17, FR-23 |
| [payments](payments/api.yaml) | GET | `/payments/{paymentId}` | `getPaymentById` | Lấy kết quả một giao dịch | FR-16, FR-17, FR-23 |
| [payments](payments/api.yaml) | POST | `/payments/{paymentId}/cash-confirmation` | `confirmCashPayment` | Xác nhận đã thu tiền mặt | FR-14 |
| [payments](payments/api.yaml) | POST | `/payments/provider-webhook` | `handlePaymentWebhook` | Nhận kết quả thanh toán từ đối tác | FR-16, FR-18 |
| [ratings](ratings/api.yaml) | POST | `/trips/{tripId}/ratings` | `createTripRating` | Đánh giá tài xế sau chuyến | FR-12 |
| [ratings](ratings/api.yaml) | GET | `/trips/{tripId}/ratings` | `listTripRatings` | Lấy đánh giá của chuyến | FR-12 |
| [notifications](notifications/api.yaml) | GET | `/notifications` | `listMyNotifications` | Lấy danh sách thông báo của tôi | FR-18, FR-19 |
| [notifications](notifications/api.yaml) | GET | `/notifications/{notificationId}` | `getNotificationById` | Lấy chi tiết thông báo | FR-18, FR-19 |
| [operations](operations/api.yaml) | GET | `/operations/transactions` | `listTransactions` | Tra cứu lịch sử giao dịch vận hành | FR-23 |
| [operations](operations/api.yaml) | POST | `/operations/support-cases` | `createSupportCase` | Ghi nhận sự cố chuyến đi | FR-22 |
| [operations](operations/api.yaml) | GET | `/operations/support-cases` | `listSupportCases` | Lấy danh sách sự cố chuyến đi | FR-22 |
| [operations](operations/api.yaml) | GET | `/operations/support-cases/{caseId}` | `getSupportCaseById` | Lấy chi tiết sự cố | FR-22 |
| [operations](operations/api.yaml) | POST | `/operations/support-cases/{caseId}/resolution` | `resolveSupportCase` | Ghi nhận kết quả hỗ trợ | FR-22, FR-26 |
| [reports](reports/api.yaml) | GET | `/reports/summary` | `getOperationalSummary` | Báo cáo số chuyến, doanh thu, tỷ lệ hoàn thành và hủy | FR-25 |
| [reports](reports/api.yaml) | GET | `/reports/driver-performance` | `listDriverPerformance` | Báo cáo hiệu quả hoạt động tài xế | FR-25 |
| [access-control](access-control/api.yaml) | GET | `/roles` | `listRoles` | Lấy danh sách vai trò | FR-24 |
| [access-control](access-control/api.yaml) | GET | `/permissions` | `listPermissions` | Lấy danh mục quyền | FR-24 |
| [access-control](access-control/api.yaml) | GET | `/users/{userId}/roles` | `getUserRoles` | Lấy các vai trò của tài khoản | FR-24 |
| [access-control](access-control/api.yaml) | PUT | `/users/{userId}/roles` | `assignUserRoles` | Gán hoặc thay thế vai trò tài khoản | FR-24, FR-26 |
| [audit-logs](audit-logs/api.yaml) | GET | `/audit-logs` | `listAuditLogs` | Tra cứu nhật ký thao tác quan trọng | FR-26 |
| [audit-logs](audit-logs/api.yaml) | GET | `/audit-logs/{auditId}` | `getAuditLogById` | Lấy chi tiết một bản ghi audit | FR-26 |
