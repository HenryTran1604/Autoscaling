### 1. **Prometheus Adapter của Kubernetes Maintainer:**

- **Mục đích**: 
  Prometheus Adapter cho Kubernetes chủ yếu được sử dụng để tích hợp Prometheus với **Kubernetes Metrics API**, cung cấp cho các hệ thống Kubernetes khả năng tự động mở rộng (autoscaling) dựa trên các chỉ số từ Prometheus.

- **External/Custom Metrics**:
  Prometheus Adapter hỗ trợ **Custom Metrics API** trong Kubernetes, cho phép bạn sử dụng các chỉ số tùy chỉnh từ Prometheus làm dữ liệu đầu vào để tự động mở rộng các tài nguyên Kubernetes như **Deployment**, **ReplicaSet**, hoặc **Pods**.

- **Cách thức hoạt động**:
  - Prometheus Adapter nhận dữ liệu từ **Prometheus** thông qua các query (PromQL) và phơi bày các chỉ số này qua **Kubernetes Custom Metrics API**.
  - Người dùng có thể cấu hình Prometheus Adapter để trích xuất các chỉ số cụ thể từ Prometheus, sau đó Kubernetes HPA (Horizontal Pod Autoscaler) có thể sử dụng các chỉ số này để quyết định việc mở rộng ứng dụng.

- **Tính năng chính**:
  - Tích hợp chặt chẽ với Prometheus và Kubernetes.
  - Hỗ trợ cho **Custom Metrics API** và **External Metrics API** của Kubernetes.
  - Được thiết kế để xử lý tải nặng, đặc biệt hữu ích khi hệ thống giám sát chủ yếu dựa trên Prometheus.
- Luồng thực hiện của prometheus adapter:
    - First, it discovers the metrics available (Discovery)
    - Then, it figures out which Kubernetes resources each metric is associated with (Association)
    - Then, it figures out how it should expose them to the custom metrics API (Naming)
    - Finally, it figures out how it should query Prometheus to get the actual numbers (Querying)

### 2. **Google Stackdriver Adapter của GCP (cloud-provider):**

- **Mục đích**: 
  Google Stackdriver Adapter (nay là Google Cloud Monitoring Adapter) được thiết kế để tích hợp Google Cloud Monitoring với **Kubernetes Metrics API**. Nó cho phép thu thập và sử dụng các chỉ số từ dịch vụ Google Cloud hoặc từ Kubernetes cluster chạy trên GCP.

- **External/Custom Metrics**:
  Stackdriver Adapter hỗ trợ cả **External Metrics API** và **Custom Metrics API**, cho phép bạn sử dụng các chỉ số tùy chỉnh được tạo ra từ môi trường Google Cloud (ví dụ: Google Cloud Pub/Sub, BigQuery) hoặc từ hệ thống bên ngoài. Những chỉ số này có thể được sử dụng cho việc tự động mở rộng tài nguyên Kubernetes.

- **Cách thức hoạt động**:
  - Adapter lấy các chỉ số từ Google Cloud Monitoring và cung cấp chúng qua **External Metrics API** hoặc **Custom Metrics API** của Kubernetes.
  - Người dùng có thể định nghĩa các chỉ số tùy chỉnh (custom metrics) trong Google Cloud Monitoring (Stackdriver) và sử dụng chúng cho Kubernetes HPA.

- **Tính năng chính**:
  - Tích hợp mạnh mẽ với toàn bộ hệ sinh thái của Google Cloud.
  - Hỗ trợ thu thập dữ liệu từ Google Cloud services cũng như các hệ thống giám sát bên ngoài.
  - Phù hợp với các hệ thống triển khai trên Google Cloud, tận dụng các dịch vụ cloud native của GCP.

### 3. **KEDA của CNCF (Kubernetes-based Event Driven Autoscaler):**

- **Mục đích**:
  KEDA là một **autoscaler** dựa trên sự kiện (event-driven autoscaler) cho Kubernetes, được quản lý bởi CNCF. KEDA không chỉ dựa trên các chỉ số giám sát như Prometheus mà còn hỗ trợ scaling dựa trên các sự kiện từ nhiều nguồn khác nhau như **Apache Kafka**, **RabbitMQ**, **AWS SQS**, **Azure Event Hub**, v.v.

- **External/Custom Metrics**:
  KEDA mở rộng khả năng tự động mở rộng của Kubernetes bằng cách thêm hỗ trợ cho **external metrics**. Nó hỗ trợ rất nhiều loại nguồn dữ liệu sự kiện và có thể xử lý các chỉ số tùy chỉnh (custom metrics) từ các hệ thống giám sát hoặc các sự kiện cụ thể.
  
  Điểm nổi bật là **ScaledObject** và **ScaledJob**, hai loại tài nguyên Kubernetes do KEDA quản lý, cho phép bạn chỉ định nguồn sự kiện hoặc chỉ số bên ngoài cần theo dõi và tự động mở rộng tài nguyên dựa trên sự kiện này.

- **Cách thức hoạt động**:
  - KEDA triển khai một thành phần gọi là **metrics server** cho phép lấy dữ liệu từ nhiều nguồn sự kiện khác nhau (Prometheus, message queues, cloud services).
  - Nó chuyển đổi các sự kiện từ các nguồn như Azure, AWS, Kafka, v.v., thành các chỉ số mà Kubernetes có thể hiểu và sử dụng để tự động mở rộng tài nguyên.
  - Các sự kiện có thể bao gồm số lượng tin nhắn chưa xử lý trong một hàng đợi (message queue), số lượng sự kiện từ hệ thống cloud, hoặc số liệu tùy chỉnh do người dùng định nghĩa.

- **Tính năng chính**:
  - Hỗ trợ cho nhiều nguồn sự kiện khác nhau (cả cloud và on-premise).
  - Có thể kết hợp với Kubernetes HPA để hỗ trợ các trường hợp mở rộng dựa trên sự kiện.
  - Đặc biệt phù hợp cho các hệ thống **event-driven**.

### So sánh chính:

| Tính năng                     | Prometheus Adapter               | Google Stackdriver Adapter       | KEDA                              |
|-------------------------------|----------------------------------|----------------------------------|-----------------------------------|
| **Mục đích chính**             | Tích hợp Prometheus với Kubernetes HPA | Tích hợp Google Cloud Monitoring với Kubernetes | Mở rộng Kubernetes dựa trên sự kiện |
| **Nguồn external/custom metrics** | Prometheus                     | Google Cloud Monitoring           | Nhiều nguồn sự kiện (Kafka, RabbitMQ, Prometheus, Cloud) |
| **Hỗ trợ External Metrics API** | Có                              | Có                              | Có                               |
| **Hỗ trợ Custom Metrics API**  | Có                              | Có                              | Không trực tiếp (chủ yếu dựa trên sự kiện) |
| **Tích hợp sự kiện**           | Không                           | Không                           | Có (nhiều nguồn sự kiện khác nhau) |
| **Tương thích Cloud**          | Chủ yếu Prometheus on-prem       | Chủ yếu GCP                      | Đa cloud (AWS, Azure, GCP)        |
| **Tích hợp Kubernetes HPA**    | Có                              | Có                              | Có (với event-driven support)     |

### Kết luận:
- **Prometheus Adapter**: Thích hợp cho những ai sử dụng Prometheus làm hệ thống giám sát chính và muốn tích hợp với Kubernetes.
- **Google Stackdriver Adapter**: Phù hợp cho những người triển khai hệ thống trên GCP và muốn tích hợp với Google Cloud Monitoring để giám sát các dịch vụ và dùng chúng cho việc tự động mở rộng.
- **KEDA**: Lý tưởng cho các hệ thống event-driven với nhiều nguồn sự kiện, giúp mở rộng ứng dụng dựa trên các sự kiện từ hệ thống cloud hoặc on-premise.

## Ứng dụng với Viettel Cloud
## a. Lấy thông tin metrics từ đâu? Ở dạng nào?
## b. Convert metrics từ đó sang HPA?
