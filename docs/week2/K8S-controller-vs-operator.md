# Kubernetes Controller and Operator
## I. Kubernetes Controller
### a. Định nghĩa
- Kubernetes Controller là một vòng lặp điều khiển liên tục giám sát trạng thái hiện tại của hệ thống và so sánh với trạng thái mong muốn (được định nghĩa trong các đối tượng Kubernetes như Deployment, ReplicaSet, ...). Nếu có bất kỳ sự khác biệt nào, controller sẽ thực hiện các hành động để đưa hệ thống về trạng thái mong muốn.
### b. Chức năng:
- **Giám sát**: Theo dõi liên tục các đối tượng Kubernetes.
- **So sánh**: So sánh trạng thái hiện tại với trạng thái mong muốn.
- **Điều chỉnh**: Thực hiện các hành động để đưa hệ thống về trạng thái mong muốn (ví dụ: tạo/xóa Pod, thay đổi số lượng replica).
- Ví dụ các controller:
    - `Deployment Controller`: Quản lý số lượng replica của một ứng dụng.
    - `ReplicaSet Controller`: Quản lý số lượng Pod với nhãn nhất định.
    - `StatefulSet Controller`: Quản lý các ứng dụng có trạng thái.
...
## II. Kubernetes Operator
### a. Định nghĩa
- Kuberntes Operator là một controller tùy chỉnh, được xây dựng để tự động hóa việc triển khai, quản lý và vận hành các ứng dụng hoặc nền tảng phức tạp trên Kubernetes.
### b. Đặc điểm:
- Domain-specific: Mỗi Operator được thiết kế để quản lý một loại ứng dụng hoặc nền tảng cụ thể.
- Custom Resource Definitions (CRDs): Operator thường định nghĩa các CRD để mô tả cấu hình và trạng thái của ứng dụng mà nó quản lý.
- Automation: Tự động hóa các tác vụ phức tạp như cài đặt, nâng cấp, backup, restore.
- Ví dụ các Operator:
    - Prometheus Operator: Quản lý hệ thống giám sát Prometheus.
    - Kafka Operator: Quản lý cụm Kafka.
    - MySQL Operator: Quản lý cơ sở dữ liệu MySQL.
## III. Sự khác biệt giữa Controller và Operator
| Tính năng | Controller | Operator |
| --------- |----------- | -------- |
| Mục đích | Quản lý các đối tượng Kubernetes cốt lõi (core) | Quản lý các ứng dụng hoặc nền tảng phức tạp |
| Phạm vi |	Hạn chế trong phạm vi Kubernetes | Có thể mở rộng ra ngoài Kubernetes để quản lý các hệ thống bên ngoài |
| Độ phức tạp | Thường đơn giản hơn | Có thể rất phức tạp, tùy thuộc vào ứng dụng được quản lý |
| Khả năng tùy chỉnh |	Ít tùy biến hơn | Rất tùy biến, có thể định nghĩa các CRD và logic điều khiển tùy chỉnh

## IV. Demo Prometheus Operator (Làm lại bài cuối kì)