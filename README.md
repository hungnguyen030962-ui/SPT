# Website Luyện Thi SPT HNUE (Toán - Ngữ Văn - Tiếng Anh)

Hệ thống luyện thi trực tuyến dành cho kỳ thi Đánh giá năng lực của Đại học Sư phạm Hà Nội (SPT HNUE). 

Để tối ưu trải nghiệm học sinh ("vào làm bài ngay"), hệ thống hoạt động hoàn toàn **không cần đăng ký/đăng nhập**. Toàn bộ tiến trình làm bài, câu hỏi sai và bookmark được tự động lưu trữ và đồng bộ hóa trực tiếp trên trình duyệt qua `localStorage`.

---

## 🌟 Tính Năng Chính

- **Luyện thi thử**: Cấu hình đề linh hoạt. Riêng môn **Toán học** cung cấp trực tiếp **6 đề thi thử chuẩn cấu trúc HNUE** cố định dài **90 phút**. Môn Văn và Anh hỗ trợ luyện tập tổng hợp.
- **Xem lại lời giải**: Chấm điểm tức thì (thang 10), hiển thị chi tiết câu đúng/sai, lời giải từng bước cho môn Toán và liệt kê các công thức liên quan.
- **Trung tâm ôn tập**:
  - **Sửa sai**: Tập hợp các câu làm sai trong các bài thi thử. Hỗ trợ làm lại; nếu giải đúng sẽ tự động gỡ ra khỏi danh sách.
  - **Bookmark**: Lưu trữ các câu hỏi tâm đắc để xem lại nhanh.
  - **Flashcard Tiếng Anh**: Học từ vựng theo phương pháp lật thẻ tương tác 3D mượt mà.

---

## ⚡ Khắc phục lỗi "Real-time chậm" (Render Free Tier)

Do sử dụng gói dịch vụ **Free Tier** của Render.com, sau 15 phút không có người sử dụng, server Render sẽ tự động ngủ (spin down). Khi người tiếp theo truy cập, sẽ mất khoảng **30 - 50 giây** để server khởi động lại (gây cảm giác phản hồi chậm ở lần nộp bài hoặc chọn đề đầu tiên).

**Để giải quyết triệt để vấn đề này hoàn toàn miễn phí:**
1. Đăng ký một tài khoản miễn phí tại **[UptimeRobot.com](https://uptimerobot.com/)** hoặc **[Cron-job.org](https://cron-job.org/)**.
2. Tạo một giám sát mới dạng **HTTP(s) GET** trỏ thẳng đến link Backend của bạn: `https://spt-backend-7u8p.onrender.com/` (hoặc link Render của bạn).
3. Thiết lập tần suất ping là **5 phút một lần**. Việc này sẽ giữ cho server của bạn luôn thức 24/7 và phản hồi ngay lập tức khi học sinh làm bài!

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
