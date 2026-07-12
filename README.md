# Website Luyện Thi SPT HNUE (Toán - Ngữ Văn - Tiếng Anh)

Hệ thống luyện thi trực tuyến dành cho kỳ thi Đánh giá năng lực của Đại học Sư phạm Hà Nội (SPT HNUE). 

Để tối ưu trải nghiệm học sinh ("vào làm bài ngay"), hệ thống hoạt động hoàn toàn **không cần đăng ký/đăng nhập**. Toàn bộ tiến trình làm bài, câu hỏi sai, bookmark và lịch sử học từ vựng được tự động lưu trữ và đồng bộ hóa trực tiếp trên trình duyệt qua `localStorage`.

---

## 🌟 Tính Năng Chính

- **Ngân hàng câu hỏi**: Tìm kiếm và lọc câu hỏi theo môn học, chuyên đề, độ khó. Hỗ trợ hiển thị công thức toán sắc nét (KaTeX) và lật xem đáp án/giải thích ngay lập tức.
- **Luyện thi thử**: Cấu hình đề linh hoạt (luyện ngẫu nhiên, luyện theo chuyên đề lựa chọn, làm đề tổng hợp) kèm đồng hồ đếm ngược thông minh tự động nộp bài khi hết giờ.
- **Xem lại lời giải**: Chấm điểm tức thì (thang 10), hiển thị chi tiết câu đúng/sai, lời giải từng bước cho môn Toán và liệt kê các công thức liên quan.
- **Thống kê học tập**: Phân tích biểu đồ tiến độ điểm thi, tổng hợp chuyên đề mạnh (đạt >= 70% đúng) và chuyên đề yếu cần cải thiện.
- **Trung tâm ôn tập**:
  - **Sửa sai**: Tập hợp các câu làm sai trong các bài thi thử. Hỗ trợ làm lại; nếu giải đúng sẽ tự động gỡ ra khỏi danh sách.
  - **Bookmark**: Lưu trữ các câu hỏi tâm đắc để xem lại nhanh.
  - **Flashcard Tiếng Anh**: Học từ vựng theo phương pháp lật thẻ tương tác 3D mượt mà.
- **Kho tài liệu Ngữ văn**: Hệ thống tác giả, tác phẩm, tóm tắt cốt truyện, giá trị nghệ thuật/nội dung, dàn ý chi tiết và từ khóa ghi nhớ nhanh.

---

## 🛠️ Công Nghệ Sử Dụng

- **Frontend**: React 19, Vite, Tailwind CSS, React Router v6, Axios, Lucide Icons, Recharts, KaTeX.
- **Backend**: FastAPI (Python), SQLAlchemy (ORM), Pydantic.
- **Database**: SQLite (phát triển local/tiện lợi không cần cấu hình phức tạp).
- **Đóng gói & Triển khai**: Docker & Docker Compose.

---

## 🚀 Hướng Dẫn Chạy Dự Án

### Cách 1: Chạy bằng Docker Compose (Khuyên dùng)
Yêu cầu hệ thống đã cài đặt Docker và Docker Compose.

1. Tại thư mục gốc của dự án, khởi chạy lệnh sau để tự động build và chạy cả frontend + backend:
   ```bash
   docker-compose up --build
   ```
2. Sau khi khởi động hoàn tất:
   - **Frontend (Giao diện người dùng)**: Truy cập tại [http://localhost](http://localhost)
   - **Backend (FastAPI Documentation)**: Truy cập tại [http://localhost:8000/docs](http://localhost:8000/docs)

*Lưu ý: Database SQLite sẽ tự động khởi tạo và được nạp (seed) sẵn dữ liệu câu hỏi mẫu phong phú cho cả 3 môn khi container backend khởi động lần đầu.*

---

### Cách 2: Chạy trực tiếp ở môi trường Local (Phát triển)

#### Chạy Backend:
Yêu cầu Python 3.10+ đã cài đặt trên máy.

1. Di chuyển vào thư mục `backend`:
   ```bash
   cd backend
   ```
2. Cài đặt các thư viện phụ thuộc:
   ```bash
   pip install -r requirements.txt
   ```
3. Chạy server FastAPI:
   ```bash
   uvicorn app.main:app --reload
   ```
   *Server backend sẽ chạy tại [http://localhost:8000](http://localhost:8000).*

#### Chạy Frontend:
Yêu cầu Node.js v18+ đã cài đặt.

1. Di chuyển vào thư mục `frontend`:
   ```bash
   cd ../frontend
   ```
2. Cài đặt các package npm:
   ```bash
   npm install
   ```
3. Khởi chạy dev server:
   ```bash
   npm run dev
   ```
   *Giao diện frontend sẽ chạy tại [http://localhost:5173](http://localhost:5173).*
