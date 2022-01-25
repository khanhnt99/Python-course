# Multithreading trong Python
## 1. Thread 
- `Thread` là một đơn vị cơ bản trong CPU. Một `thread` sẽ chia sẻ với các `thread` khác trong cùng 1 process về thông tin data, các dữ liệu của mình.
- Việc tạo ra thread giúp cho các chương trình có thể chạy được nhiều công việc một lúc.
- `Process` là quá trình hoạt động của 1 ứng dụng. Process chứ thông tin tài nguyên, trạng thái thực hiện của chương trình.
- `Thread` là một bước điều hành bên trong một process. `Thread` là một khối các câu lệnh (instructions) độc lập trong một tiến trình và có thể được lập lịch từ hệ điều hành. Một `process` có thể chứa nhiều thread bên trong nó, một thread có thể làm bất cứ nhiệm vụ gì một process có thể làm.
- Nhiều `thread` nằm trong cùng một `process` dùng một không gian bộ nhớ giống nhau, trong khi process thì không. Điều này cho phép các thread đọc và viết cùng 1 kiểu cấu trúc dữ liệu.
- Giao thức giữa các process `(IPC - inter-process communication)`.
- Ngoài các tài nguyên riêng của `thread` (các biến cục bộ trong hàm), các thread chia sẻ tài nguyên chung của process. 

## 2. Multithreading
- Một chương trình đa luồng chứa hai hoặc nhiều phần mà có thể chạy đồng thời và mỗi phần có thể xử lý tác vụ khác nhau tại cùng 1 thời điểm.
- Mỗi Thread đều có vòng đời chung là bắt đầu, chạy và kết thúc. Một thread có thể bị ngắt, hoặc tạm dừng trong khi các thread khác đang chạy - được gọi là `yielding`.
- Module Threading cung cấp nhiều hỗ trợ mạnh mẽ, ngoài các phương thức có trong thread module, threading module còn bổ sung một số phương thức khác đó là:
    + `threading.activeCount()` trả về số lượng thread đang active.
    + `threading.currentThread()` trả về số lượng thread trong Thread control của Caller.
    + `threading.enumerate()` trả về một danh sách tất cả đối tượng thread đang active.

- Bên cạnh đó, threading Module có lớp Thread để triển khai đa luồng. Lớp này có các phương thức sau:
    + `run()` là entry point cho một thread.
    + `start()` bắt đầu 1 thread.
    + `join([time])` đợi cho các thread kết thúc.
    + `isAlive()` kiểm tra xem một thread có đang thực thi hay không.
    + `getName()` trả về tên một thread.

- `Daemon thread` thường được dùng khi không còn cách đơn giản nào để dừng được thread này (infinitive loop), hoặc ngắt giữa trừng mà không ảnh hưởng đến dữ liệu.

