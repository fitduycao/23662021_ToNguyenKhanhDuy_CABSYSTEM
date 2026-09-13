# Truy vết Functional Requirements → API

Có endpoint đại diện không có nghĩa FR đã được lập trình hoặc nghiệm thu. Các chính sách TBD vẫn cần xác nhận.

| FR | Function/operationId | Xử lý nội bộ / ghi chú |
|---|---|---|
| FR-01 | `registerCustomer`, `login`, `getMyProfile`, `updateMyProfile` | Xem quyền, schema, phản hồi và TBD trong từng operation. |
| FR-02 | `registerDriver`, `login`, `getMyProfile`, `updateMyProfile`, `createDriver`, `getDriverById`, `updateDriver` | Xem quyền, schema, phản hồi và TBD trong từng operation. |
| FR-03 | `createVehicle`, `listVehicles`, `getVehicleById`, `updateVehicle` | Xem quyền, schema, phản hồi và TBD trong từng operation. |
| FR-04 | `updateDriverAvailability`, `updateDriverLocation`, `getDriverLocation` | Xem quyền, schema, phản hồi và TBD trong từng operation. |
| FR-05 | `listServiceTypes`, `createTrip` | Xem quyền, schema, phản hồi và TBD trong từng operation. |
| FR-06 | `createTrip` | dispatchTrip: chọn/ưu tiên ứng viên theo TBD-02. |
| FR-07 | `listMyDispatchOffers`, `getDispatchOffer`, `acceptDispatchOffer`, `declineDispatchOffer` | Xem quyền, schema, phản hồi và TBD trong từng operation. |
| FR-08 | `createTrip`, `declineDispatchOffer` | dispatchTrip: timeout và tìm tiếp tự động, no_driver khi hết điều kiện. |
| FR-09 | `getTripById`, `trackTrip`, `acceptDispatchOffer` | Xem quyền, schema, phản hồi và TBD trong từng operation. |
| FR-10 | `updateTripStatus`, `listTripStatusHistory` | Xem quyền, schema, phản hồi và TBD trong từng operation. |
| FR-11 | `listTrips`, `getTripById`, `getTripFare`, `listTripPayments` | Xem quyền, schema, phản hồi và TBD trong từng operation. |
| FR-12 | `createTripRating`, `listTripRatings` | Xem quyền, schema, phản hồi và TBD trong từng operation. |
| FR-13 | `updateTripStatus`, `getTripFare` | calculateCompletedTripFare: chạy khi hoàn thành; GET chỉ đọc kết quả. |
| FR-14 | `createTripPayment`, `confirmCashPayment` | Xem quyền, schema, phản hồi và TBD trong từng operation. |
| FR-15 | `createTripPayment` | Xem quyền, schema, phản hồi và TBD trong từng operation. |
| FR-16 | `getPaymentById`, `handlePaymentWebhook` | Xem quyền, schema, phản hồi và TBD trong từng operation. |
| FR-17 | `createTripPayment`, `listTripPayments`, `getPaymentById` | Xem quyền, schema, phản hồi và TBD trong từng operation. |
| FR-18 | `createTrip`, `updateTripStatus`, `acceptDispatchOffer`, `handlePaymentWebhook`, `listMyNotifications`, `getNotificationById` | deliverNotifications: đủ các sự kiện cho khách; GET chỉ đọc lại. |
| FR-19 | `updateTripStatus`, `cancelTrip`, `listMyDispatchOffers`, `listMyNotifications`, `getNotificationById` | deliverNotifications: offer mới và thay đổi chuyến cho tài xế. |
| FR-20 | `createUser`, `listUsers`, `getUserById`, `updateUser`, `deleteUser`, `changeUserStatus`, `createDriver`, `listDrivers`, `updateDriver`, `deactivateDriver`, `createVehicle`, `listVehicles`, `getVehicleById`, `updateVehicle`, `deactivateVehicle` | Xem quyền, schema, phản hồi và TBD trong từng operation. |
| FR-21 | `listDrivers`, `getDriverById`, `getDriverLocation`, `listTrips`, `getTripById`, `listTripStatusHistory` | Xem quyền, schema, phản hồi và TBD trong từng operation. |
| FR-22 | `createSupportCase`, `listSupportCases`, `getSupportCaseById`, `resolveSupportCase` | SupportCase là đề xuất; thao tác khắc phục nghiệp vụ cụ thể còn TBD-11. |
| FR-23 | `listTripPayments`, `getPaymentById`, `listTransactions` | Xem quyền, schema, phản hồi và TBD trong từng operation. |
| FR-24 | `changeUserStatus`, `listRoles`, `listPermissions`, `getUserRoles`, `assignUserRoles` | Kiểm tra quyền tại mọi endpoint; quản lý vai trò là đề xuất cụ thể hóa. |
| FR-25 | `getOperationalSummary`, `listDriverPerformance` | Xem quyền, schema, phản hồi và TBD trong từng operation. |
| FR-26 | `resolveSupportCase`, `assignUserRoles`, `listAuditLogs`, `getAuditLogById` | recordAudit chạy tự động cho danh mục thao tác đã duyệt; GET chỉ tra cứu. |
| FR-27 | `cancelTrip` | Hủy theo TBD-04, không mặc định quyền/phí. |
