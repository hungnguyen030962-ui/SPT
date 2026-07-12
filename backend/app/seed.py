import sys
import os

# Add the parent directory to python path to import app correctly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.core.database import SessionLocal, Base, engine
from app.models.question import Question
from app.models.literature import LiteratureMaterial
from app.models.flashcard import EnglishFlashcard

def generate_math_exam(exam_num):
    exam_name = f"Đề số {exam_num}"
    questions = []
    
    # 1. Lượng giác
    k1 = exam_num * 2
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Lượng giác",
        difficulty="medium",
        content=f"Tìm tập nghiệm của phương trình \\(\\sin({k1}x) = 1\\).",
        options=[
            f"A. \\(x = \\frac{{\\pi}}{{{k1}}} + k\\frac{{\\pi}}{{{exam_num}}}\\)",
            f"B. \\(x = \\frac{{\\pi}}{{{k1 * 2}}} + k\\frac{{\\pi}}{{{exam_num}}}\\)",
            f"C. \\(x = \\frac{{\\pi}}{{{k1 * 2}}} + k2\\pi\\)",
            f"D. \\(x = \\frac{{\\pi}}{{{k1}}} + k2\\pi\\)"
        ],
        correct_answer="B",
        explanation=f"Ta có \\(\\sin({k1}x) = 1 \\Leftrightarrow {k1}x = \\frac{{\\pi}}{{2}} + k2\\pi \\Leftrightarrow x = \\frac{{\\pi}}{{{k1 * 2}}} + k\\frac{{\\pi}}{{{exam_num}}}\\) (với \\(k \\in \\mathbb{{Z}}\\)).",
        step_by_step=[
            {"step": "Áp dụng công thức nghiệm lượng giác", "detail": f"\\(\\sin(u) = 1 \\Leftrightarrow u = \\frac{{\\pi}}{{2}} + k2\\pi\\)."},
            {"step": "Thay u và giải tìm x", "detail": f"Thay \\(u = {k1}x\\), ta được: \\({k1}x = \\frac{{\\pi}}{{2}} + k2\\pi \\Leftrightarrow x = \\frac{{\\pi}}{{{k1 * 2}}} + \\frac{{k2\\pi}}{{{k1}}} \\Leftrightarrow x = \\frac{{\\pi}}{{{k1 * 2}}} + k\\frac{{\\pi}}{{{exam_num}}}\\)."}
        ],
        formulas=["\\sin(u) = 1 \\Leftrightarrow u = \\frac{\\pi}{2} + k2\\pi"]
    ))
    
    # 2. Giới hạn - Liên tục
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Giới hạn",
        difficulty="easy",
        content=f"Tính giới hạn \\(L = \\lim_{{x \\to 2}} \\frac{{x^2 - {exam_num + 3}x + {2 * exam_num + 2}}}{{x - 2}}\\).",
        options=[
            f"A. \\({2 - exam_num}\\)",
            f"B. \\({1 - exam_num}\\)",
            f"C. \\({3 - exam_num}\\)",
            f"D. Vô cực"
        ],
        correct_answer="B",
        explanation=f"Phân tích tử số thành nhân tử: \\(x^2 - {exam_num + 3}x + {2 * exam_num + 2} = (x - 2)(x - {exam_num + 1})\\). Rút gọn phân thức và tính giới hạn khi \\(x \\to 2\\), ta được \\(2 - ({exam_num} + 1) = {1 - exam_num}\\).",
        step_by_step=[
            {"step": "Phân tích nhân tử ở tử số", "detail": f"Tử số có nghiệm \\(x=2\\) và \\(x={exam_num + 1}\\), do đó: \\(x^2 - {exam_num + 3}x + {2 * exam_num + 2} = (x-2)(x - ({exam_num + 1}))\\)."},
            {"step": "Rút gọn nhân tử chung", "detail": f"Với \\(x \\neq 2\\), biểu thức bằng \\(x - {exam_num + 1}\\)."},
            {"step": "Tính giới hạn", "detail": f"\\(L = \\lim_{{x \\to 2}} (x - {exam_num + 1}) = 2 - {exam_num} - 1 = {1 - exam_num}\\)."}
        ],
        formulas=["\\lim_{x \\to a} \\frac{f(x)}{g(x)} = \\lim_{x \\to a} f'(x) \\text{ nếu có dạng } \\frac{0}{0}"]
    ))
    
    # 3. Đạo hàm
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Đạo hàm",
        difficulty="easy",
        content=f"Tính đạo hàm của hàm số \\(y = \\ln(x^2 + {exam_num})\\).",
        options=[
            f"A. \\(y' = \\frac{{2x}}{{x^2 + {exam_num}}}\\)",
            f"B. \\(y' = \\frac{{1}}{{x^2 + {exam_num}}}\\)",
            f"C. \\(y' = \\frac{{2x + {exam_num}}}{{x^2 + {exam_num}}}\\)",
            f"D. \\(y' = \\frac{{x}}{{x^2 + {exam_num}}}\\)"
        ],
        correct_answer="A",
        explanation=f"Sử dụng công thức đạo hàm hàm hợp \\((\\ln u)' = \\frac{{u'}}{{u}}\\). Ở đây \\(u = x^2 + {exam_num} \\Rightarrow u' = 2x\\). Do đó \\(y' = \\frac{{2x}}{{x^2 + {exam_num}}}\\).",
        step_by_step=[
            {"step": "Xác định hàm số hợp", "detail": f"Đặt \\(u(x) = x^2 + {exam_num}\\)."},
            {"step": "Áp dụng công thức đạo hàm", "detail": f"\\(y' = \\frac{{u'}}{{u}} = \\frac{{(x^2 + {exam_num})'}}{{x^2 + {exam_num}}} = \\frac{{2x}}{{x^2 + {exam_num}}}\\)."}
        ],
        formulas=["(\\ln u)' = \\frac{u'}{u}"]
    ))
    
    # 4. Khảo sát hàm số - Sự biến thiên
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Khảo sát hàm số",
        difficulty="medium",
        content=f"Hàm số \\(y = x^3 - 3({exam_num})x^2 + 1\\) nghịch biến trên khoảng nào?",
        options=[
            f"A. \\((0; {exam_num * 2})\\)",
            f"B. \\((0; {exam_num})\\)",
            f"C. \\((-\\infty; 0)\\)",
            f"D. \\(({exam_num}; +\\infty)\\)"
        ],
        correct_answer="A" if exam_num % 2 == 0 else "B",
        explanation=f"Đạo hàm \\(y' = 3x^2 - 6({exam_num})x = 3x(x - {exam_num * 2})\\). Hệ số \\(a > 0\\) nên hàm số nghịch biến trên khoảng giữa hai nghiệm của \\(y'=0\\), tức là \\((0; {exam_num * 2})\\).",
        step_by_step=[
            {"step": "Tính đạo hàm y'", "detail": f"\\(y' = 3x^2 - 6({exam_num})x\\)."},
            {"step": "Tìm nghiệm y' = 0", "detail": f"\\(3x(x - {exam_num * 2}) = 0 \\Leftrightarrow x = 0 \\text{{ hoặc }} x = {exam_num * 2}\\)."},
            {"step": "Xét dấu đạo hàm", "detail": f"Trong khoảng hai nghiệm \\((0; {exam_num * 2})\\), đạo hàm mang dấu âm (do hệ số \\(a = 3 > 0\\)). Do đó hàm số nghịch biến."}
        ],
        formulas=["y' < 0 \\Rightarrow \\text{Hàm số nghịch biến}"]
    ))
    
    # 5. Cực trị hàm số
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Khảo sát hàm số",
        difficulty="medium",
        content=f"Tìm số điểm cực trị của đồ thị hàm số \\(y = x^4 - 2({exam_num})x^2 + 3\\).",
        options=["A. 1", "B. 2", "C. 3", "D. 0"],
        correct_answer="C" if exam_num > 0 else "A",
        explanation=f"Đạo hàm \\(y' = 4x^3 - 4({exam_num})x = 4x(x^2 - {exam_num})\\). Vì \\({exam_num} > 0\\), phương trình \\(y' = 0\\) có 3 nghiệm phân biệt \\(x = 0\\) và \\(x = \\pm\\sqrt{{{exam_num}}}\\). Do đó hàm số có 3 điểm cực trị.",
        step_by_step=[
            {"step": "Tính đạo hàm y'", "detail": f"\\(y' = 4x^3 - 4({exam_num})x = 4x(x^2 - {exam_num})\\)."},
            {"step": "Giải phương trình y' = 0", "detail": f"\\(4x(x^2 - {exam_num}) = 0 \\Leftrightarrow x = 0\\) hoặc \\(x = \\pm\\sqrt{{{exam_num}}}\\) (3 nghiệm phân biệt)."},
            {"step": "Kết luận cực trị", "detail": "Do phương trình đạo hàm đổi dấu qua 3 nghiệm đơn phân biệt nên đồ thị có 3 điểm cực trị."}
        ],
        formulas=["y' = 0 \\text{ có } 3 \\text{ nghiệm đơn } \\Rightarrow 3 \\text{ điểm cực trị}"]
    ))
    
    # 6. Hàm số mũ & Logarit
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Hàm số mũ & Logarit",
        difficulty="medium",
        content=f"Tìm tập nghiệm của bất phương trình \\(\\log_{{2}}(x - {exam_num}) < 3\\).",
        options=[
            f"A. \\(({exam_num}; {exam_num + 8})\\)",
            f"B. \\((-\\infty; {exam_num + 8})\\)",
            f"C. \\(({exam_num}; {exam_num + 9})\\)",
            f"D. \\(({exam_num}; +\\infty)\\)"
        ],
        correct_answer="A",
        explanation=f"Điều kiện xác định: \\(x - {exam_num} > 0 \\Leftrightarrow x > {exam_num}\\). Bất phương trình tương đương: \\(x - {exam_num} < 2^3 = 8 \\Leftrightarrow x < {exam_num + 8}\\). Kết hợp điều kiện ta được \\({exam_num} < x < {exam_num + 8}\\).",
        step_by_step=[
            {"step": "Tìm điều kiện xác định", "detail": f"Biểu thức trong logarit phải dương: \\(x - {exam_num} > 0 \\Leftrightarrow x > {exam_num}\\)."},
            {"step": "Giải bất phương trình", "detail": f"\\(\\log_{{2}}(x - {exam_num}) < 3 \\Leftrightarrow x - {exam_num} < 2^3 \\Leftrightarrow x < {exam_num + 8}\\)."},
            {"step": "Kết hợp điều kiện", "detail": f"Giao hai điều kiện: \\(x \\in ({exam_num}; {exam_num + 8})\\)."}
        ],
        formulas=["\\log_a f(x) < b \\Leftrightarrow 0 < f(x) < a^b \\text{ (với } a > 1\\text{)}"]
    ))
    
    # 7. Nguyên hàm
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Tích phân",
        difficulty="easy",
        content=f"Tìm nguyên hàm của hàm số \\(f(x) = e^{{{exam_num}x}} + {exam_num * 2}x\\).",
        options=[
            f"A. \\(F(x) = \\frac{{1}}{{{exam_num}}}e^{{{exam_num}x}} + {exam_num}x^2 + C\\)",
            f"B. \\(F(x) = e^{{{exam_num}x}} + {exam_num}x^2 + C\\)",
            f"C. \\(F(x) = \\frac{{1}}{{{exam_num}}}e^{{{exam_num}x}} + {exam_num * 2}x^2 + C\\)",
            f"D. \\(F(x) = {exam_num}e^{{{exam_num}x}} + {exam_num}x^2 + C\\)"
        ],
        correct_answer="A",
        explanation=f"Ta có \\(\\int e^{{{exam_num}x}} dx = \\frac{{1}}{{{exam_num}}}e^{{{exam_num}x}} + C_1\\) và \\(\\int {exam_num * 2}x dx = {exam_num}x^2 + C_2\\). Do đó nguyên hàm là \\(F(x) = \\frac{{1}}{{{exam_num}}}e^{{{exam_num}x}} + {exam_num}x^2 + C\\).",
        step_by_step=[
            {"step": "Tìm nguyên hàm từng thành phần", "detail": f"Nguyên hàm của \\(e^{{{exam_num}x}}\\) là \\(\\frac{{1}}{{{exam_num}}}e^{{{exam_num}x}}\\). Nguyên hàm của \\({exam_num * 2}x\\) là \\({exam_num}x^2\\)."},
            {"step": "Cộng các kết quả", "detail": f"\\(F(x) = \\frac{{1}}{{{exam_num}}}e^{{{exam_num}x}} + {exam_num}x^2 + C\\)."}
        ],
        formulas=["\\int e^{ax} dx = \\frac{1}{a}e^{ax} + C", "\\int x dx = \\frac{x^2}{2} + C"]
    ))
    
    # 8. Tích phân
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Tích phân",
        difficulty="easy",
        content=f"Tính tích phân \\(I = \\int_{{0}}^{{1}} (x + {exam_num}) dx\\).",
        options=[
            f"A. \\({exam_num} + 0.5\\)",
            f"B. \\({exam_num}\\)",
            f"C. \\({exam_num} + 1\\)",
            f"D. \\({exam_num} - 0.5\\)"
        ],
        correct_answer="A",
        explanation=f"Ta có nguyên hàm là \\(F(x) = \\frac{{x^2}}{{2}} + {exam_num}x\\). Áp dụng công thức Leibniz: \\(I = F(1) - F(0) = (0.5 + {exam_num}) - 0 = {exam_num} + 0.5\\).",
        step_by_step=[
            {"step": "Tìm nguyên hàm", "detail": f"\\(\\int (x + {exam_num}) dx = \\frac{{x^2}}{{2}} + {exam_num}x\\)."},
            {"step": "Thế cận tích phân", "detail": f"Thế 1 vào: \\(\\frac{{1}}{{2}} + {exam_num} = {exam_num} + 0.5\\). Thế 0 vào: \\(0\\). Trừ hai kết quả: \\({exam_num} + 0.5\\)."}
        ],
        formulas=["\\int_{a}^{b} f(x) dx = F(b) - F(a)"]
    ))
    
    # 9. Diện tích & Thể tích hình phẳng
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Tích phân",
        difficulty="medium",
        content=f"Tính thể tích vật thể tròn xoay khi quay hình phẳng giới hạn bởi đồ thị hàm số \\(y = {exam_num}x\\), trục hoành, đường thẳng \\(x=0\\) và \\(x=1\\) quanh trục \\(Ox\\).",
        options=[
            f"A. \\(\\frac{{{exam_num ** 2}\\pi}}{{3}}\\)",
            f"B. \\(\\frac{{{exam_num}\\pi}}{{3}}\\)",
            f"C. \\(\\frac{{{exam_num ** 2}\\pi}}{{2}}\\)",
            f"D. \\({exam_num ** 2}\\pi\\)"
        ],
        correct_answer="A",
        explanation=f"Thể tích \\(V = \\pi \\int_{{0}}^{{1}} y^2 dx = \\pi \\int_{{0}}^{{1}} {exam_num ** 2}x^2 dx = \\pi \\left. \\frac{{{exam_num ** 2}x^3}}{{3}} \\right|_{{0}}^{{1}} = \\frac{{{exam_num ** 2}\\pi}}{{3}}\\).",
        step_by_step=[
            {"step": "Thiết lập công thức tính thể tích", "detail": f"\\(V = \\pi \\int_{{0}}^{{1}} [f(x)]^2 dx = \\pi \\int_{{0}}^{{1}} ({exam_num}x)^2 dx = \\pi \\int_{{0}}^{{1}} {exam_num ** 2}x^2 dx\\)."},
            {"step": "Tính nguyên hàm và thế cận", "detail": f"\\(V = \\pi \\left[ \\frac{{{exam_num ** 2}x^3}}{{3}} \\right]_0^1 = \\frac{{{exam_num ** 2}\\pi}}{{3}} - 0 = \\frac{{{exam_num ** 2}\\pi}}{{3}}\\)."}
        ],
        formulas=["V = \\pi \\int_{a}^{b} [f(x)]^2 dx"]
    ))
    
    # 10. Số phức
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Số phức",
        difficulty="easy",
        content=f"Cho hai số phức \\(z_1 = 1 + {exam_num}i\\) và \\(z_2 = 2 - i\\). Tìm phần thực của số phức \\(w = z_1 + z_2\\).",
        options=["A. 3", "B. 1", "C. 2", f"D. \\({exam_num - 1}\\)"],
        correct_answer="A",
        explanation=f"Ta có \\(w = (1 + 2) + ({exam_num} - 1)i = 3 + ({exam_num - 1})i\\). Phần thực của \\(w\\) là 3.",
        step_by_step=[
            {"step": "Cộng hai số phức", "detail": f"Phần thực cộng phần thực: \\(1 + 2 = 3\\). Phần ảo cộng phần ảo: \\(({exam_num} - 1)i\\)."},
            {"step": "Xác định phần thực", "detail": "Phần thực là số đứng độc lập không đi kèm với đơn vị ảo i, tức là 3."}
        ],
        formulas=["(a + bi) + (c + di) = (a + c) + (b + d)i"]
    ))
    
    # 11. Tọa độ điểm trong không gian
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Hình học Oxyz",
        difficulty="easy",
        content=f"Trong không gian \\(Oxyz\\), cho điểm \\(A(1; {exam_num}; -2)\\) and \\(B(3; 2; {exam_num * 2})\\). Tìm tọa độ vectơ \\(\\vec{{AB}}\\).",
        options=[
            f"A. \\((2; {2 - exam_num}; {exam_num * 2 + 2})\\)",
            f"B. \\((4; {exam_num + 2}; {exam_num * 2 - 2})\\)",
            f"C. \\((2; {exam_num - 2}; {exam_num * 2 + 2})\\)",
            f"D. \\((2; {2 - exam_num}; {exam_num * 2 - 2})\\)"
        ],
        correct_answer="A",
        explanation=f"Tọa độ vectơ \\(\\vec{{AB}} = (x_B - x_A; y_B - y_A; z_B - z_A) = (3 - 1; 2 - {exam_num}; {exam_num * 2} - (-2)) = (2; {2 - exam_num}; {exam_num * 2 + 2})\\).",
        step_by_step=[
            {"step": "Áp dụng công thức tính tọa độ vectơ", "detail": "\\(\\vec{{AB}} = (x_B - x_A; y_B - y_A; z_B - z_A)\\)."},
            {"step": "Thế số và tính toán", "detail": f"\\(\\vec{{AB}} = (3-1; 2-{exam_num}; {exam_num*2} - (-2)) = (2; {2-exam_num}; {exam_num*2+2})\\)."}
        ],
        formulas=["\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A)"]
    ))
    
    # 12. Mặt phẳng Oxyz
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Hình học Oxyz",
        difficulty="medium",
        content=f"Trong không gian \\(Oxyz\\), viết phương trình mặt phẳng đi qua điểm \\(M(1; 1; 1)\\) và nhận \\(\\vec{{n}} = (2; -{exam_num}; 1)\\) làm vectơ pháp tuyến.",
        options=[
            f"A. \\(2x - {exam_num}y + z + {exam_num - 3} = 0\\)",
            f"B. \\(2x - {exam_num}y + z - {exam_num - 3} = 0\\)",
            f"C. \\(2x - {exam_num}y + z + {3 - exam_num} = 0\\)",
            f"D. \\(2x + {exam_num}y + z - {3 + exam_num} = 0\\)"
        ],
        correct_answer="A",
        explanation=f"Mặt phẳng có dạng \\(2(x-1) - {exam_num}(y-1) + 1(z-1) = 0 \\Leftrightarrow 2x - {exam_num}y + z - 2 + {exam_num} - 1 = 0 \\Leftrightarrow 2x - {exam_num}y + z + {exam_num - 3} = 0\\).",
        step_by_step=[
            {"step": "Sử dụng công thức mặt phẳng đi qua 1 điểm", "detail": "\\(A(x-x_0) + B(y-y_0) + C(z-z_0) = 0\\)."},
            {"step": "Thay số vào công thức", "detail": f"Thay điểm M(1;1;1) và vectơ chỉ phương: \\(2(x-1) - {exam_num}(y-1) + 1(z-1) = 0\\)."},
            {"step": "Rút gọn phương trình", "detail": f"\\(2x - {exam_num}y + z - 2 + {exam_num} - 1 = 0 \\Rightarrow 2x - {exam_num}y + z + {exam_num - 3} = 0\\)."}
        ],
        formulas=["A(x-x_0) + B(y-y_0) + C(z-z_0) = 0"]
    ))
    
    # 13. Đường thẳng Oxyz
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Hình học Oxyz",
        difficulty="medium",
        content=f"Trong không gian \\(Oxyz\\), cho đường thẳng \\(d: \\frac{{x - 1}}{{2}} = \\frac{{y + 2}}{{-{exam_num}}} = \\frac{{z}}{{1}}\\). Tìm vectơ chỉ phương của đường thẳng \\(d\\).",
        options=[
            f"A. \\(\\vec{{u}} = (2; -{exam_num}; 1)\\)",
            f"B. \\(\\vec{{u}} = (1; -2; 0)\\)",
            f"C. \\(\\vec{{u}} = (2; {exam_num}; 1)\\)",
            f"D. \\(\\vec{{u}} = (-2; {exam_num}; 1)\\)"
        ],
        correct_answer="A",
        explanation=f"Từ phương trình chính tắc của đường thẳng \\(\\frac{{x-x_0}}{{a}} = \\frac{{y-y_0}}{{b}} = \\frac{{z-z_0}}{{c}}\\), vectơ chỉ phương là \\(\\vec{{u}} = (a; b; c) = (2; -{exam_num}; 1)\\).",
        step_by_step=[
            {"step": "Xác định các hệ số ở mẫu số", "detail": f"Mẫu số của các biểu thức phân số lần lượt là: 2, -{exam_num}, 1."}
        ],
        formulas=["\\frac{x-x_0}{a} = \\frac{y-y_0}{b} = \\frac{z-z_0}{c} \\Rightarrow \\vec{u} = (a; b; c)"]
    ))
    
    # 14. Tổ hợp - Xác suất
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Tổ hợp - Xác suất",
        difficulty="medium",
        content=f"Một hộp có {exam_num + 5} viên bi đỏ và 5 viên bi xanh. Lấy ngẫu nhiên ra 2 viên bi. Tính xác suất để lấy được 2 viên bi màu xanh.",
        options=[
            f"A. \\(\\frac{{10}}{{{(exam_num + 10) * (exam_num + 9)}}}\\)",
            f"B. \\(\\frac{{20}}{{{(exam_num + 10) * (exam_num + 9)}}}\\)",
            f"C. \\(\\frac{{5}}{{{exam_num + 10}}}\\)",
            f"D. \\(\\frac{{1}}{{{exam_num + 10}}}\\)"
        ],
        correct_answer="B",
        explanation=f"Tổng số bi là \\({exam_num + 10}\\). Số cách chọn 2 bi bất kỳ là \\(C_{{{exam_num + 10}}}^2 = \\frac{{({exam_num + 10})({exam_num + 9})}}{{2}}\\). Số cách chọn 2 bi xanh là \\(C_5^2 = 10\\). Xác suất cần tìm: \\(P = \\frac{{10}}{{\\frac{{({exam_num + 10})({exam_num + 9})}}{{2}}}} = \\frac{{20}}{{({exam_num + 10})({exam_num + 9})}}\\).",
        step_by_step=[
            {"step": "Tính không gian mẫu", "detail": f"Tổng số bi là \\({exam_num + 10}\\) viên. Số cách chọn ngẫu nhiên 2 viên bi: \\(n(\\Omega) = C_{{{exam_num + 10}}}^2 = \\frac{{({exam_num + 10})({exam_num + 9})}}{{2}}\\)."},
            {"step": "Tính số kết quả thuận lợi", "detail": "Số cách chọn ra 2 viên bi xanh từ 5 viên xanh: \\(n(A) = C_5^2 = 10\\)."},
            {"step": "Tính xác suất", "detail": f"\\(P(A) = \\frac{{n(A)}}{{n(\\Omega)}} = \\frac{{10 \\cdot 2}}{{({exam_num + 10})({exam_num + 9})}} = \\frac{{20}}{{({exam_num + 10})({exam_num + 9})}}\\)."}
        ],
        formulas=["P(A) = \\frac{n(A)}{n(\\Omega)}", "C_n^k = \\frac{n!}{k!(n-k)!}"]
    ))
    
    # 15. Cấp số cộng & Cấp số nhân
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Cấp số cộng - Cấp số nhân",
        difficulty="easy",
        content=f"Cho cấp số nhân \\((u_n)\\) có \\(u_1 = 3\\) và công bội \\(q = {exam_num}\\). Tìm số hạng thứ 3 \\(u_3\\).",
        options=[
            f"A. \\({3 * exam_num ** 2}\\)",
            f"B. \\({3 * exam_num}\\)",
            f"C. \\({3 * exam_num ** 3}\\)",
            f"D. \\(3 + {exam_num * 2}\\)"
        ],
        correct_answer="A",
        explanation=f"Công thức số hạng tổng quát của cấp số nhân: \\(u_n = u_1 \\cdot q^{{n-1}}\\). Với \\(n=3\\), ta có \\(u_3 = u_1 \\cdot q^2 = 3 \\cdot {exam_num}^2 = {3 * exam_num ** 2}\\).",
        step_by_step=[
            {"step": "Áp dụng công thức cấp số nhân", "detail": "\\(u_n = u_1 \\cdot q^{{n-1}}\\)."},
            {"step": "Thay số và tính toán", "detail": f"\\(u_3 = u_1 \\cdot q^2 = 3 \\cdot {exam_num}^2 = {3 * exam_num ** 2}\\)."}
        ],
        formulas=["u_n = u_1 \\cdot q^{n-1}"]
    ))
    
    # 16. Thể tích hình chóp
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Hình học không gian",
        difficulty="medium",
        content=f"Cho khối chóp \\(S.ABC\\) có diện tích đáy \\(S_{{ABC}} = {exam_num * 3}a^2\\) và chiều cao \\(h = 4a\\). Tính thể tích \\(V\\) của khối chóp \\(S.ABC\\).",
        options=[
            f"A. \\({exam_num * 4}a^3\\)",
            f"B. \\({exam_num * 12}a^3\\)",
            f"C. \\({exam_num * 2}a^3\\)",
            f"D. \\({exam_num * 6}a^3\\)"
        ],
        correct_answer="A",
        explanation=f"Thể tích khối chóp: \\(V = \\frac{{1}}{{3}} B \\cdot h = \\frac{{1}}{{3}} \\cdot {exam_num * 3}a^2 \\cdot 4a = {exam_num * 4}a^3\\).",
        step_by_step=[
            {"step": "Áp dụng công thức thể tích hình chóp", "detail": f"\\(V = \\frac{{1}}{{3}} S_{{đáy}} \\cdot h\\)."},
            {"step": "Thế số vào công thức", "detail": f"\\(V = \\frac{{1}}{{3}} \\cdot ({exam_num * 3}a^2) \\cdot 4a = {exam_num * 4}a^3\\)."}
        ],
        formulas=["V = \\frac{1}{3} B / h"]
    ))
    
    return questions

def seed_db():
    print("Recreating database tables...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        print("Seeding questions...")
        
        # 1. MATHEMATICS EXAMS (6 EXAMS - 16 QUESTIONS EACH)
        math_questions = []
        for i in range(1, 7):
            math_questions.extend(generate_math_exam(i))

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
            )
        ]
        for q in eng_questions:
            db.add(q)

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
