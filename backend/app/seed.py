import sys
import os

# Add the parent directory to python path to import app correctly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.core.database import SessionLocal, Base, engine
from app.models.question import Question
from app.models.literature import LiteratureMaterial
from app.models.flashcard import EnglishFlashcard

def seed_db():
    print("Recreating database tables...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        print("Seeding questions...")
        
        # 1. MATHEMATICS EXAMS (6 EXAMS - ĐỀ SỐ 1 ĐẾN ĐỀ SỐ 6)
        math_questions = []

        # --- ĐỀ SỐ 1 ---
        math_questions.extend([
            Question(
                subject="math",
                exam_name="Đề số 1",
                topic="Lượng giác",
                difficulty="medium",
                content="Hàm số \\(y = 5 + 4 \\sin 2x \\cos 2x\\) có tất cả bao nhiêu giá trị nguyên?",
                options=["A. 3", "B. 4", "C. 5", "D. 6"],
                correct_answer="C",
                explanation="Ta có \\(y = 5 + 2 \\sin 4x\\). Vì \\(-1 \\leq \\sin 4x \\leq 1\\) nên \\(3 \\leq y \\leq 7\\). Các giá trị nguyên của \\(y\\) là \\(\\{3; 4; 5; 6; 7\\}\\). Tổng cộng có 5 giá trị nguyên.",
                step_by_step=[
                    {"step": "Biến đổi công thức nhân đôi", "detail": "\\(y = 5 + 4\\sin 2x\\cos 2x = 5 + 2(2\\sin 2x\\cos 2x) = 5 + 2\\sin 4x\\)."},
                    {"step": "Tìm khoảng giá trị", "detail": "Do \\(-1 \\leq \\sin 4x \\leq 1\\) nên \\(-2 \\leq 2\\sin 4x \\leq 2 \\Rightarrow 3 \\leq 5 + 2\\sin 4x \\leq 7\\)."},
                    {"step": "Đếm các giá trị nguyên", "detail": "Các giá trị nguyên thuộc đoạn \\([3; 7]\\) là 3, 4, 5, 6, 7. Có tất cả 5 giá trị."}
                ],
                formulas=["\\sin 2\\alpha = 2\\sin\\alpha\\cos\\alpha", "-1 \\leq \\sin \\theta \\leq 1"]
            ),
            Question(
                subject="math",
                exam_name="Đề số 1",
                topic="Khảo sát hàm số",
                difficulty="easy",
                content="Cho hàm số \\(y = f(x)\\) có bảng biến thiên: cực đại tại \\(x=-1, y=5\\) và cực tiểu tại \\(x=3, y=1\\). Giá trị cực tiểu của hàm số bằng bao nhiêu?",
                options=["A. 1", "B. 3", "C. 5", "D. -1"],
                correct_answer="A",
                explanation="Từ bảng biến thiên, ta thấy hàm số đạt cực tiểu tại điểm \\(x_{CT} = 3\\) và giá trị cực tiểu tương ứng là \\(y_{CT} = f(3) = 1\\).",
                step_by_step=[
                    {"step": "Đọc bảng biến thiên", "detail": "Tại điểm cực tiểu \\(x = 3\\), giá trị hàm số đi xuống đến giá trị cực tiểu tương ứng là 1 rồi đi lên."}
                ],
                formulas=["y_{CT} \\text{ là giá trị cực tiểu của hàm số tại điểm cực tiểu } x_{CT}"]
            ),
            Question(
                subject="math",
                exam_name="Đề số 1",
                topic="Hàm số mũ & Logarit",
                difficulty="medium",
                content="Tìm tập nghiệm \\(S\\) của phương trình \\(e^{6x} - 3e^{3x} + 2 = 0\\).",
                options=[
                    "A. \\(S = \\{0; \\ln 2\\}\\)",
                    "B. \\(S = \\left\\{0; \\frac{\\ln 2}{3}\\right\\}\\)",
                    "C. \\(S = \\left\\{1; \\frac{\\ln 2}{3}\\right\\}\\)",
                    "D. \\(S = \\{1; \\ln 2\\}\\)"
                ],
                correct_answer="B",
                explanation="Đặt \\(t = e^{3x} > 0\\), phương trình trở thành \\(t^2 - 3t + 2 = 0 \\Leftrightarrow t=1 \\text{ hoặc } t=2\\). Từ đó giải ra nghiệm \\(x\\).",
                step_by_step=[
                    {"step": "Đặt ẩn phụ", "detail": "Đặt \\(t = e^{3x}\\) (điều kiện \\(t > 0\\)). Phương trình viết lại thành: \\(t^2 - 3t + 2 = 0\\)."},
                    {"step": "Giải phương trình bậc hai", "detail": "Nghiệm của phương trình: \\(t = 1\\) (nhận) hoặc \\(t = 2\\) (nhận)."},
                    {"step": "Tìm nghiệm x", "detail": "Với \\(t = 1 \\Rightarrow e^{3x} = 1 \\Leftrightarrow 3x = 0 \\Leftrightarrow x = 0\\). Với \\(t = 2 \\Rightarrow e^{3x} = 2 \\Leftrightarrow 3x = \\ln 2 \\Leftrightarrow x = \\frac{\\ln 2}{3}\\)."}
                ],
                formulas=["e^{2u} = (e^u)^2", "e^{A} = B \\Leftrightarrow A = \\ln B"]
            ),
            Question(
                subject="math",
                exam_name="Đề số 1",
                topic="Tích phân",
                difficulty="medium",
                content="Biết \\(\\int_{0}^{3} f(x) dx = \\frac{5}{3}\\) và \\(\\int_{0}^{4} f(t) dt = \\frac{3}{5}\\). Tính tích phân \\(I = \\int_{3}^{4} f(u) du\\).",
                options=["A. \\(\\frac{8}{15}\\)", "B. \\(\\frac{14}{15}\\)", "C. \\(\\frac{17}{15}\\)", "D. \\(-\\frac{16}{15}\\)"],
                correct_answer="D",
                explanation="Ta có \\(\\int_{0}^{4} f(x) dx = \\int_{0}^{3} f(x) dx + \\int_{3}^{4} f(x) dx \\Rightarrow \\int_{3}^{4} f(x) dx = \\int_{0}^{4} f(x) dx - \\int_{0}^{3} f(x) dx\\).",
                step_by_step=[
                    {"step": "Sử dụng tính chất tích phân", "detail": "Công thức nối cận tích phân: \\(\\int_{a}^{b} f(x)dx + \\int_{b}^{c} f(x)dx = \\int_{a}^{c} f(x)dx\\)."},
                    {"step": "Tính tích phân cần tìm", "detail": "\\(I = \\int_{3}^{4} f(u) du = \\int_{0}^{4} f(x)dx - \\int_{0}^{3} f(x)dx = \\frac{3}{5} - \\frac{5}{3} = \\frac{9 - 25}{15} = -\\frac{16}{15}\\)."}
                ],
                formulas=["\\int_{a}^{c} f(x)dx = \\int_{a}^{b} f(x)dx + \\int_{b}^{c} f(x)dx"]
            ),
            Question(
                subject="math",
                exam_name="Đề số 1",
                topic="Hình học Oxyz",
                difficulty="medium",
                content="Trong không gian \\(Oxyz\\), cho mặt phẳng \\((P): x + 2y - 3z - 4 = 0\\) và điểm \\(A(1; -2; -3)\\). Phương trình đường thẳng đi qua \\(A\\) và vuông góc với mặt phẳng \\((P)\\) là gì?",
                options=[
                    "A. \\(\\frac{x-1}{1} = \\frac{y+2}{2} = \\frac{z+3}{-3}\\)",
                    "B. \\(\\frac{x+1}{1} = \\frac{y-2}{2} = \\frac{z-3}{-3}\\)",
                    "C. \\(\\frac{x-1}{1} = \\frac{y-2}{-2} = \\frac{z+3}{-3}\\)",
                    "D. \\(\\frac{x-1}{1} = \\frac{y+2}{-2} = \\frac{z+3}{-3}\\)"
                ],
                correct_answer="A",
                explanation="Đường thẳng vuông góc với mặt phẳng \\((P)\\) sẽ có vectơ chỉ phương \\(\\vec{u}\\) cùng phương với vectơ pháp tuyến \\(\\vec{n}_P = (1; 2; -3)\\). Viết phương trình chính tắc đi qua \\(A(1; -2; -3)\\).",
                step_by_step=[
                    {"step": "Xác định vectơ pháp tuyến", "detail": "Mặt phẳng \\((P)\\) có vectơ pháp tuyến \\(\\vec{n}_P = (1; 2; -3)\\)."},
                    {"step": "Xác định vectơ chỉ phương đường thẳng", "detail": "Do đường thẳng vuông góc với \\((P)\\) nên chỉ phương \\(\\vec{u} = \\vec{n}_P = (1; 2; -3)\\)."},
                    {"step": "Viết phương trình chính tắc", "detail": "Đường thẳng đi qua \\(A(1; -2; -3)\\) có phương trình: \\(\\frac{x-1}{1} = \\frac{y+2}{2} = \\frac{z+3}{-3}\\)."}
                ],
                formulas=["d \\perp (P) \\Rightarrow \\vec{u}_d = \\vec{n}_P"]
            )
        ])

        # --- ĐỀ SỐ 2 ---
        math_questions.extend([
            Question(
                subject="math",
                exam_name="Đề số 2",
                topic="Khảo sát hàm số",
                difficulty="medium",
                content="Tìm số giao điểm của đồ thị hàm số \\(y = x^3 - 3x^2 + 4\\) và đường thẳng \\(y = 4\\).",
                options=["A. 1", "B. 2", "C. 3", "D. 0"],
                correct_answer="C",
                explanation="Phương trình hoành độ giao điểm: \\(x^3 - 3x^2 + 4 = 4 \\Leftrightarrow x^2(x - 3) = 0 \\Leftrightarrow x=0\\) hoặc \\(x=3\\). Tuy nhiên ta có 2 nghiệm phân biệt giao điểm.",
                step_by_step=[
                    {"step": "Lập phương trình hoành độ giao điểm", "detail": "\\(x^3 - 3x^2 + 4 = 4\\)."},
                    {"step": "Giải phương trình", "detail": "\\(x^3 - 3x^2 = 0 \\Leftrightarrow x^2(x - 3) = 0 \\Leftrightarrow x = 0 \\text{ hoặc } x = 3\\). Có 2 giao điểm phân biệt."}
                ],
                formulas=["f(x) = g(x) \\text{ xác định hoành độ giao điểm}"]
            ),
            Question(
                subject="math",
                exam_name="Đề số 2",
                topic="Số phức",
                difficulty="easy",
                content="Cho số phức \\(z = 3 - 2i\\). Tìm môđun của số phức \\(z\\).",
                options=["A. 13", "B. \\(\\sqrt{13}\\)", "C. 5", "D. \\(\\sqrt{5}\\)"],
                correct_answer="B",
                explanation="Môđun số phức \\(z = a + bi\\) tính theo công thức \\(|z| = \\sqrt{a^2 + b^2} = \\sqrt{3^2 + (-2)^2} = \\sqrt{13}\\).",
                step_by_step=[
                    {"step": "Áp dụng công thức tính môđun", "detail": "\\(|z| = \\sqrt{3^2 + (-2)^2} = \\sqrt{9 + 4} = \\sqrt{13}\\)."}
                ],
                formulas=["|z| = \\sqrt{a^2 + b^2}"]
            )
        ])

        # --- ĐỀ SỐ 3 ---
        math_questions.extend([
            Question(
                subject="math",
                exam_name="Đề số 3",
                topic="Khối đa diện",
                difficulty="medium",
                content="Cho khối lăng trụ đứng có diện tích đáy bằng \\(3a^2\\) và chiều cao bằng \\(4a\\). Thể tích của khối lăng trụ bằng bao nhiêu?",
                options=["A. \\(4a^3\\)", "B. \\(12a^3\\)", "C. \\(6a^3\\)", "D. \\(8a^3\\)"],
                correct_answer="B",
                explanation="Thể tích khối lăng trụ tính theo công thức \\(V = B \\cdot h = 3a^2 \\cdot 4a = 12a^3\\).",
                step_by_step=[
                    {"step": "Tính thể tích lăng trụ", "detail": "\\(V = S_{đáy} \\cdot h = 3a^2 \\cdot 4a = 12a^3\\)."}
                ],
                formulas=["V_{lăng trụ} = B \\cdot h"]
            ),
            Question(
                subject="math",
                exam_name="Đề số 3",
                topic="Tổ hợp - Xác suất",
                difficulty="easy",
                content="Có bao nhiêu cách chọn ra 2 học sinh từ một nhóm gồm 10 học sinh?",
                options=["A. 90", "B. 45", "C. 20", "D. 10"],
                correct_answer="B",
                explanation="Chọn 2 học sinh từ 10 học sinh không phân biệt thứ tự là số tổ hợp chập 2 của 10: \\(C_{10}^2 = \\frac{10 \\cdot 9}{2} = 45\\).",
                step_by_step=[
                    {"step": "Tính số tổ hợp", "detail": "\\(C_{10}^2 = \\frac{10!}{2!8!} = 45\\)."}
                ],
                formulas=["C_n^k = \\frac{n!}{k!(n-k)!}"]
            )
        ])

        # --- ĐỀ SỐ 4 ---
        math_questions.extend([
            Question(
                subject="math",
                exam_name="Đề số 4",
                topic="Mặt nón - Mặt trụ - Mặt cầu",
                difficulty="easy",
                content="Diện tích xung quanh của hình trụ có bán kính đáy \\(r = 3\\) và chiều cao \\(h = 5\\) bằng bao nhiêu?",
                options=["A. \\(15\\pi\\)", "B. \\(30\\pi\\)", "C. \\(45\\pi\\)", "D. \\(90\\pi\\)"],
                correct_answer="B",
                explanation="Diện tích xung quanh hình trụ: \\(S_{xq} = 2\\pi r h = 2\\pi \\cdot 3 \\cdot 5 = 30\\pi\\).",
                step_by_step=[
                    {"step": "Tính diện tích", "detail": "\\(S_{xq} = 2\\pi \\cdot 3 \\cdot 5 = 30\\pi\\)."}
                ],
                formulas=["S_{xq} = 2\\pi r h"]
            )
        ])

        # --- ĐỀ SỐ 5 ---
        math_questions.extend([
            Question(
                subject="math",
                exam_name="Đề số 5",
                topic="Cấp số cộng - Cấp số nhân",
                difficulty="easy",
                content="Cho cấp số cộng \\((u_n)\\) có \\(u_1 = 2\\) và công sai \\(d = 3\\). Tìm số hạng \\(u_4\\).",
                options=["A. 11", "B. 14", "C. 8", "D. 5"],
                correct_answer="A",
                explanation="Ta có \\(u_n = u_1 + (n-1)d \\Rightarrow u_4 = u_1 + 3d = 2 + 3 \\cdot 3 = 11\\).",
                step_by_step=[
                    {"step": "Tính u4", "detail": "\\(u_4 = 2 + 3(3) = 11\\)."}
                ],
                formulas=["u_n = u_1 + (n-1)d"]
            )
        ])

        # --- ĐỀ SỐ 6 ---
        math_questions.extend([
            Question(
                subject="math",
                exam_name="Đề số 6",
                topic="Hàm số mũ & Logarit",
                difficulty="easy",
                content="Tìm tập xác định của hàm số \\(y = \\log_2 (x - 3)\\).",
                options=[
                    "A. \\((3; +\\infty)\\)",
                    "B. \\([3; +\\infty)\\)",
                    "C. \\(\\mathbb{R} \\setminus \\{3\\}\\)",
                    "D. \\((-\\infty; 3)\\)"
                ],
                correct_answer="A",
                explanation="Điều kiện xác định của biểu thức dưới dấu logarit: \\(x - 3 > 0 \\Leftrightarrow x > 3\\). Vậy tập xác định là \\((3; +\\infty)\\).",
                step_by_step=[
                    {"step": "Đặt điều kiện xác định", "detail": "\\(x - 3 > 0 \\Leftrightarrow x > 3\\)."}
                ],
                formulas=["\\log_a f(x) \\text{ xác định khi } f(x) > 0"]
            )
        ])

        for q in math_questions:
            db.add(q)

        # 2. LITERATURE QUESTIONS (General questions)
        lit_questions = [
            Question(
                subject="literature",
                topic="Tác phẩm văn xuôi",
                difficulty="easy",
                content="Tác phẩm 'Vợ nhặt' của nhà văn Kim Lân được in trong tập truyện nào sau đây?",
                options=[
                    "A. Con chó xấu xí",
                    "B. Quê người",
                    "C. Chiếc thuyền ngoài xa",
                    "D. Gió lạnh đầu mùa"
                ],
                correct_answer="A",
                explanation="Truyện ngắn 'Vợ nhặt' tiền thân là một chương của tiểu thuyết 'Xóm ngụ cư', sau khi hòa bình lập lại tác giả viết lại và in trong tập truyện 'Con chó xấu xí' (1962).",
                step_by_step=[],
                formulas=[]
            ),
            Question(
                subject="literature",
                topic="Thơ ca kháng chiến",
                difficulty="medium",
                content="Trong bài thơ 'Tây Tiến' của Quang Dũng, hình tượng 'đoàn binh không mọc tóc' phản ánh thực tế khốc liệt nào của cuộc chiến đấu xưa?",
                options=[
                    "A. Tác hại của bệnh sốt rét rừng hiểm nghèo",
                    "B. Người lính chủ động cạo đầu để thuận tiện hành quân",
                    "C. Hình phạt của quân đội",
                    "D. Ảnh hưởng của bom hóa học"
                ],
                correct_answer="A",
                explanation="Hình ảnh 'không mọc tóc' phản ánh chân thực cuộc sống gian khổ nơi chiến trường miền Tây hiểm trở, nơi người lính phải đối mặt với căn bệnh sốt rét tàn phá thể chất khiến tóc rụng sạch.",
                step_by_step=[],
                formulas=[]
            ),
            Question(
                subject="literature",
                topic="Tác phẩm văn xuôi",
                difficulty="easy",
                content="Nhân vật Tràng trong tác phẩm 'Vợ nhặt' làm nghề gì ở xóm ngụ cư để kiếm sống?",
                options=[
                    "A. Kéo xe bò thuê",
                    "B. Bốc vác ở bến sông",
                    "C. Làm ruộng",
                    "D. Buôn bán nhỏ"
                ],
                correct_answer="A",
                explanation="Trong truyện ngắn 'Vợ nhặt', Tràng làm nghề kéo xe bò thuê chở thóc cho liên đoàn để nuôi mẹ già và bản thân qua những ngày đói kém.",
                step_by_step=[],
                formulas=[]
            )
        ]
        for q in lit_questions:
            db.add(q)

        # 3. ENGLISH QUESTIONS (General questions)
        eng_questions = [
            Question(
                subject="english",
                topic="Vocabulary",
                difficulty="easy",
                content="She was so ________ in her studies that she completely forgot about the appointment.",
                options=[
                    "A. absorbed",
                    "B. interested",
                    "C. occupied",
                    "D. distracted"
                ],
                correct_answer="A",
                explanation="'Be absorbed in something/doing something' means very interested in something and giving it all your attention (say mê, chìm đắm trong học tập).",
                step_by_step=[],
                formulas=[]
            ),
            Question(
                subject="english",
                topic="Grammar",
                difficulty="medium",
                content="If you ________ hard, you would have passed the exam last week.",
                options=[
                    "A. studied",
                    "B. had studied",
                    "C. would study",
                    "D. study"
                ],
                correct_answer="B",
                explanation="This is Conditional Sentence Type 3, expressing a hypothetical condition in the past. Structure: If + S + had + V3/ed, S + would + have + V3/ed.",
                step_by_step=[],
                formulas=[]
            ),
            Question(
                subject="english",
                topic="Reading",
                difficulty="medium",
                content="According to the passage, what is the primary cause of global warming?",
                passage="Global warming is a major environmental challenge. Over the past century, global temperatures have risen by about 1 degree Celsius. The primary driver of this increase is the accumulation of greenhouse gases, such as carbon dioxide and methane, in the atmosphere. These gases trap heat from the sun. Humans contribute to this accumulation through the burning of fossil fuels (like coal, oil, and natural gas) for electricity, heat, and transportation.",
                options=[
                    "A. Natural solar cycles",
                    "B. The accumulation of greenhouse gases",
                    "C. Industrial water pollution",
                    "D. Volcanic activity"
                ],
                correct_answer="B",
                explanation="The passage explicitly states: 'The primary driver of this increase is the accumulation of greenhouse gases... in the atmosphere.'",
                step_by_step=[],
                formulas=[]
            )
        ]
        for q in eng_questions:
            db.add(q)

        print("Seeding literature materials...")
        
        # LITERATURE MATERIALS
        materials = [
            LiteratureMaterial(
                title="Vợ nhặt",
                author="Kim Lân",
                epoch="1945 - 1975 (Thời kỳ kháng chiến chống Pháp)",
                genre="Truyện ngắn",
                summary="Tác phẩm lấy bối cảnh nạn đói năm 1945. Tràng, một chàng trai nghèo khổ làm nghề kéo xe thuê ở xóm ngụ cư, giữa cơn đói hoành hành đã đưa một người đàn bà đói rách về làm vợ ('vợ nhặt'). Sự kiện này khiến xóm ngụ cư ngạc nhiên, bà cụ Tứ (mẹ Tràng) vừa mừng vừa lo. Dù đối mặt với cái chết cận kề, họ vẫn yêu thương, nương tựa vào nhau, nhen nhóm hy vọng về một tương lai tươi sáng qua hình ảnh lá cờ đỏ của Việt Minh cuối tác phẩm.",
                content_value="Phơi bày thảm cảnh nạn đói năm 1945 do phát xít Nhật và thực dân Pháp gây ra. Ca ngợi vẻ đẹp nhân bản sâu sắc của người lao động nghèo: tình người ấm áp, khát vọng sống, khát vọng hạnh phúc mãnh liệt và niềm tin vững chắc vào cách mạng.",
                art_value="Cách xây dựng tình huống truyện độc đáo ('nhặt' vợ giữa ngày đói). Nghệ thuật miêu tả tâm lý nhân vật tinh tế, tự nhiên. Ngôn ngữ mộc mạc, giản dị, đậm chất nông thôn Bắc Bộ.",
                outline=[
                    {"section": "1. Hoàn cảnh xuất hiện nhân vật Tràng và sự việc 'nhặt vợ'", "content": "Bối cảnh ngày đói u ám, tiếng quạ kêu, người chết đói như ngả rạ. Tràng kéo xe thóc và buông lời hò đùa tình cờ đưa thị về làm vợ."},
                    {"section": "2. Đoạn đường đưa vợ nhặt về xóm ngụ cư", "content": "Sự ngạc nhiên của người dân xóm ngụ cư. Vẻ ngượng ngùng nhưng ẩn chứa niềm vui len lỏi trong lòng Tràng và thị."}
                ],
                keywords=["Nạn đói 1945", "Tình cảm gia đình", "Khát vọng hạnh phúc", "Tình huống nhặt vợ", "Bà cụ Tứ"]
            ),
            LiteratureMaterial(
                title="Tây Tiến",
                author="Quang Dũng",
                epoch="1948 (Thời kỳ đầu kháng chiến chống Pháp)",
                genre="Thơ trữ tình",
                summary="Bài thơ được Quang Dũng sáng tác tại Phù Lưu Chanh khi ông phải rời xa đơn vị cũ (đoàn quân Tây Tiến). Tây Tiến là tên một trung đoàn thành lập năm 1947 để phối hợp với quân đội Lào bảo vệ biên giới Việt - Lào. Bài thơ tái hiện ký ức về thiên nhiên Tây Bắc hùng vĩ, hiểm trở mà thơ mộng, cùng cuộc sống chiến đấu vô cùng gian khổ nhưng ngập tràn vẻ đẹp lãng mạn, bi tráng của những người lính Tây Tiến hào hoa.",
                content_value="Khắc họa thành công bức tượng đài bất tử về người lính Tây Tiến với vẻ đẹp kiêu hùng, hào hoa, sẵn sàng hiến dâng tuổi trẻ cho Tổ quốc. Tình yêu sâu nặng của tác giả đối với vùng đất Tây Bắc và đồng đội.",
                art_value="Bút pháp lãng mạn kết hợp chất bi tráng độc đáo. Ngôn ngữ giàu nhạc điệu, hình ảnh sáng tạo sắc nét, sử dụng hiệu quả hệ thống từ Hán Việt gợi không khí cổ kính, trang nghiêm.",
                outline=[
                    {"section": "1. Những chặng đường hành quân gian khổ và thiên nhiên miền Tây", "content": "Ký ức về dốc cao hiểm trở 'Dốc lên khúc khuỷu dốc thăm thẳm', mưa rừng sương mù, hình ảnh người lính gục lên súng mũ bỏ quên đời."},
                    {"section": "2. Kỷ niệm ấm áp tình quân dân và cảnh sông nước thơ mộng", "content": "Đêm liên hoan văn nghệ lung linh 'Doanh trại bừng lên hội đuốc hoa' và cảnh chiều sương Châu Mộc thơ mộng hư ảo."}
                ],
                keywords=["Thiên nhiên hùng vĩ", "Chân dung người lính", "Hào hoa lãng mạn", "Bi tráng"]
            )
        ]
        for m in materials:
            db.add(m)

        print("Seeding English flashcards...")
        
        # ENGLISH FLASHCARDS
        flashcards = [
            EnglishFlashcard(word="Absorbed", ipa="[əbˈzɔːbd]", meaning="Say mê, chăm chú, đắm chìm", part_of_speech="Adjective", example="She was totally absorbed in her novel.", topic="Education"),
            EnglishFlashcard(word="Curriculum", ipa="[kəˈrɪkjələm]", meaning="Chương trình giảng dạy", part_of_speech="Noun", example="The school is introducing a new science curriculum.", topic="Education"),
            EnglishFlashcard(word="Sustainable", ipa="[səˈsteɪnəbl]", meaning="Bền vững, có thể duy trì lâu dài", part_of_speech="Adjective", example="The government is promoting sustainable energy sources.", topic="Environment")
        ]
        for f in flashcards:
            db.add(f)

        db.commit()
        print("Database seeded successfully!")

    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}")
        raise e
    finally:
        db.close()

if __name__ == "__main__":
    seed_db()
