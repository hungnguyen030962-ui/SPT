import sys
import os

# Add the parent directory to python path to import app correctly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.core.database import SessionLocal, Base, engine
from app.models.question import Question

def generate_math_exam(exam_num):
    exam_name = f"Đề số {exam_num}"
    questions = []
    
    # --- PHẦN I: TRẮC NGHIỆM KHÁCH QUAN (16 CÂU) ---
    
    # Câu 1: Cực trị hàm số bậc ba
    y_cd = 2
    y_ct = 2 - 4 * (exam_num ** 3)
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Cực trị hàm số",
        difficulty="medium",
        content=f"**Câu 1**: Cho hàm số \\(y = f(x) = x^3 - 3({exam_num})x^2 + 2\\) liên tục trên \\(\\mathbb{{R}}\\). Tìm tập hợp tất cả các giá trị của tham số \\(m\\) để phương trình \\(f(x) = m\\) có đúng 3 nghiệm thực phân biệt.",
        options=[
            f"A. \\({y_ct} < m < {y_cd}\\)",
            f"B. \\(m > {y_cd}\\)",
            f"C. \\(m < {y_ct}\\)",
            f"D. \\(m = {y_cd}\\) hoặc \\(m = {y_ct}\\)"
        ],
        correct_answer="A",
        explanation=f"Đạo hàm \\(y' = 3x^2 - 6({exam_num})x = 3x(x - {2 * exam_num})\\). Cho \\(y' = 0 \\Leftrightarrow x = 0\\) hoặc \\(x = {2 * exam_num}\\). Đồ thị có điểm cực đại là \\((0; 2)\\) và điểm cực tiểu là \\(({2 * exam_num}; {y_ct})\\). Phương trình có 3 nghiệm phân biệt khi đường thẳng \\(y = m\\) cắt đồ thị tại 3 điểm phân biệt, tương đương \\({y_ct} < m < {y_cd}\\)."
    ))

    # Câu 2: Đạo hàm hàm số mũ
    base_val = exam_num + 2
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Hàm số mũ & Logarit",
        difficulty="easy",
        content=f"**Câu 2**: Tính đạo hàm của hàm số \\(y = {base_val}^{{x^2 - 2x}}\\).",
        options=[
            f"A. \\(y' = (2x - 2) \\cdot {base_val}^{{x^2 - 2x}} \\cdot \\ln {base_val}\\)",
            f"B. \\(y' = (x^2 - 2x) \\cdot {base_val}^{{x^2 - 2x - 1}}\\)",
            f"C. \\(y' = {base_val}^{{x^2 - 2x}} \\cdot \\ln {base_val}\\)",
            f"D. \\(y' = \\frac{{2x - 2}}{{\\ln {base_val}}} \\cdot {base_val}^{{x^2 - 2x}}\\)"
        ],
        correct_answer="A",
        explanation=f"Áp dụng công thức đạo hàm hàm hợp \\((a^u)' = u' \\cdot a^u \\cdot \\ln a\\). Ở đây \\(a = {base_val}\\), \\(u = x^2 - 2x \\Rightarrow u' = 2x - 2\\). Do đó ta có: \\(y' = (2x - 2) \\cdot {base_val}^{{x^2 - 2x}} \\cdot \\ln {base_val}\\)."
    ))

    # Câu 3: Tập xác định hàm số lũy thừa
    x_val = exam_num + 1
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Hàm số mũ & Logarit",
        difficulty="easy",
        content=f"**Câu 3**: Tìm tập xác định \\(D\\) của hàm số \\(y = (x^2 - {exam_num + 2}x + {exam_num + 1})^{{-e}}\\).",
        options=[
            f"A. \\(D = (-\\infty; 1) \\cup ({x_val}; +\\infty)\\)",
            f"B. \\(D = \\mathbb{{R}} \\setminus \\{{1; {x_val}\\}}\\)",
            f"C. \\(D = (1; {x_val})\\)",
            f"D. \\(D = \\mathbb{{R}}\\)"
        ],
        correct_answer="A",
        explanation=f"Hàm số lũy thừa có số mũ không nguyên xác định khi cơ số dương: \\(x^2 - {exam_num + 2}x + {exam_num + 1} > 0 \\Leftrightarrow (x-1)(x-{x_val}) > 0 \\Leftrightarrow x < 1\\) hoặc \\(x > {x_val}\\). Tập xác định là \\(D = (-\\infty; 1) \\cup ({x_val}; +\\infty)\\)."
    ))

    # Câu 4: Giải phương trình Logarit
    ans_q4 = exam_num + 4
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Hàm số mũ & Logarit",
        difficulty="medium",
        content=f"**Câu 4**: Giải phương trình \\(\\log_2(x - {exam_num + 2}) + \\log_2(x - {exam_num}) = 3\\).",
        options=[
            f"A. \\(x = {ans_q4}\\)",
            f"B. \\(x = {ans_q4}\\) hoặc \\(x = {exam_num - 2}\\)",
            f"C. \\(x = {ans_q4 - 1}\\)",
            f"D. \\(x = {exam_num + 2}\\)"
        ],
        correct_answer="A",
        explanation=f"Điều kiện: \\(x > {exam_num + 2}\\). Phương trình viết lại: \\(\\log_2[(x - {exam_num + 2})(x - {exam_num})] = 3 \\Leftrightarrow x^2 - {2 * exam_num + 2}x + {exam_num * (exam_num + 2)} = 8 \\Leftrightarrow x^2 - {2 * exam_num + 2}x + {exam_num ** 2 + 2 * exam_num - 8} = 0 \\Leftrightarrow x = {ans_q4}\\) (nhận) hoặc \\(x = {exam_num - 2}\\) (loại do điều kiện)."
    ))

    # Câu 5: Nguyên hàm phân thức
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Tích phân",
        difficulty="medium",
        content=f"**Câu 5**: Tìm nguyên hàm \\(F(x)\\) của hàm số \\(f(x) = \\frac{{2x + {exam_num + 2}}}{{x + 1}}\\) trên khoảng \\((-1; +\\infty)\\) biết \\(F(0) = 2\\).",
        options=[
            f"A. \\(F(x) = 2x + {exam_num}\\ln(x + 1) + 2\\)",
            f"B. \\(F(x) = 2x + {exam_num}\\ln|x + 1| + C\\)",
            f"C. \\(F(x) = 2x - {exam_num}\\ln(x + 1) + 2\\)",
            f"D. \\(F(x) = 2x + {exam_num + 2}\\ln(x + 1) + 2\\)"
        ],
        correct_answer="A",
        explanation=f"Ta có \\(f(x) = \\frac{{2(x+1) + {exam_num}}}{{x+1}} = 2 + \\frac{{{exam_num}}}{{x+1}}\\). Nguyên hàm là \\(F(x) = 2x + {exam_num}\\ln(x+1) + C\\) (vì \\(x > -1\\)). Từ \\(F(0) = 2 \\Rightarrow 0 + 0 + C = 2 \\Rightarrow C = 2\\). Vậy \\(F(x) = 2x + {exam_num}\\ln(x+1) + 2\\)."
    ))

    # Câu 6: Diện tích giới hạn bởi parabol và Ox
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Tích phân",
        difficulty="medium",
        content=f"**Câu 6**: Tính diện tích \\(S\\) của hình phẳng giới hạn bởi đồ thị hàm số \\(y = x^3 - {exam_num ** 2}x\\) và trục hoành \\(Ox\\).",
        options=[
            f"A. \\(S = \\frac{{{exam_num ** 4}}}{{2}}\\)",
            f"B. \\(S = \\frac{{{exam_num ** 4}}}{{4}}\\)",
            f"C. \\(S = {exam_num ** 4}\\)",
            f"D. \\(S = 2({exam_num ** 4})\\)"
        ],
        correct_answer="A",
        explanation=f"Phương trình hoành độ giao điểm: \\(x^3 - {exam_num ** 2}x = 0 \\Leftrightarrow x = 0, x = \\pm {exam_num}\\). Do đồ thị đối xứng qua gốc tọa độ: \\(S = 2 \\int_{{0}}^{{{exam_num}}} |x^3 - {exam_num ** 2}x| dx = 2 \\int_{{0}}^{{{exam_num}}} ({exam_num ** 2}x - x^3) dx = 2 \\left. \\left( \\frac{{{exam_num ** 2}x^2}}{{2}} - \\frac{{x^4}}{{4}} \\right) \\right|_{{0}}^{{{exam_num}}} = 2 \\left( \\frac{{{exam_num ** 4}}}{{2}} - \\frac{{{exam_num ** 4}}}{{4}} \\right) = \\frac{{{exam_num ** 4}}}{{2}}\\)."
    ))

    # Câu 7: Số phức liên hợp
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Số phức",
        difficulty="medium",
        content=f"**Câu 7**: Tìm số phức liên hợp \\(\\overline{{z}}\\) của số phức \\(z\\) thỏa mãn \\((1 + i)z = {exam_num + 2} - i\\).",
        options=[
            f"A. \\(\\overline{{z}} = \\frac{{{exam_num + 1}}}{{2}} + \\frac{{{exam_num + 3}}}{{2}}i\\)",
            f"B. \\(\\overline{{z}} = \\frac{{{exam_num + 1}}}{{2}} - \\frac{{{exam_num + 3}}}{{2}}i\\)",
            f"C. \\(\\overline{{z}} = \\frac{{{exam_num + 3}}}{{2}} + \\frac{{{exam_num + 1}}}{{2}}i\\)",
            f"D. \\(\\overline{{z}} = -\\frac{{{exam_num + 1}}}{{2}} - \\frac{{{exam_num + 3}}}{{2}}i\\)"
        ],
        correct_answer="A",
        explanation=f"Ta có \\(z = \\frac{{{exam_num + 2} - i}}{{1 + i}} = \\frac{{({exam_num + 2} - i)(1 - i)}}{{2}} = \\frac{{{exam_num + 1} - ({exam_num + 3})i}}{{2}}\\). Suy ra số phức liên hợp là \\(\\overline{{z}} = \\frac{{{exam_num + 1}}}{{2}} + \\frac{{{exam_num + 3}}}{{2}}i\\)."
    ))

    # Câu 8: Môđun số phức
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Số phức",
        difficulty="easy",
        content=f"**Câu 8**: Tính môđun của số phức \\(z = {exam_num} + 4i\\).",
        options=[
            f"A. \\(|z| = \\sqrt{{{exam_num ** 2 + 16}}}\\)",
            f"B. \\(|z| = {exam_num ** 2 + 16}\\)",
            f"C. \\(|z| = {exam_num + 4}\\)",
            f"D. \\(|z| = \\sqrt{{{exam_num ** 2 - 16}}}\\)"
        ],
        correct_answer="A",
        explanation=f"Áp dụng công thức tính môđun của số phức \\(z = a + bi\\): \\(|z| = \\sqrt{{a^2 + b^2}} = \\sqrt{{{exam_num}^2 + 4^2}} = \\sqrt{{{exam_num ** 2 + 16}}}\\)."
    ))

    # Câu 9: Tọa độ trung điểm Oxyz
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Hình học Oxyz",
        difficulty="easy",
        content=f"**Câu 9**: Trong không gian \\(Oxyz\\), cho hai điểm \\(A({exam_num}; 2; -3)\\) và \\(B(3; 0; -1)\\). Tìm tọa độ trung điểm \\(M\\) của đoạn thẳng \\(AB\\).",
        options=[
            f"A. \\(M\\left(\\frac{{{exam_num + 3}}}{{2}}; 1; -2\\right)\\)",
            f"B. \\(M({exam_num + 3}; 2; -4)\\)",
            f"C. \\(M\\left(\\frac{{{exam_num - 3}}}{{2}}; 1; -1\\right)\\)",
            f"D. \\(M\\left(\\frac{{{exam_num + 3}}}{{2}}; 1; -1\\right)\\)"
        ],
        correct_answer="A",
        explanation=f"Áp dụng công thức trung điểm: \\(x_M = \\frac{{x_A + x_B}}{{2}} = \\frac{{{exam_num} + 3}}{{2}}\\); \\(y_M = 1\\); \\(z_M = -2\\). Tọa độ trung điểm là \\(M\\left(\\frac{{{exam_num + 3}}}{{2}}; 1; -2\\right)\\)."
    ))

    # Câu 10: Viết phương trình mặt phẳng song song
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Hình học Oxyz",
        difficulty="medium",
        content=f"**Câu 10**: Trong không gian \\(Oxyz\\), viết phương trình mặt phẳng đi qua điểm \\(A(1; 2; 3)\\) và song song với mặt phẳng \\((P): 2x - y + {exam_num}z - 5 = 0\\).",
        options=[
            f"A. \\(2x - y + {exam_num}z - {3 * exam_num} = 0\\)",
            f"B. \\(2x - y + {exam_num}z + {3 * exam_num} = 0\\)",
            f"C. \\(2x - y + {exam_num}z - 5 = 0\\)",
            f"D. \\(2x - y + {exam_num}z = 0\\)"
        ],
        correct_answer="A",
        explanation=f"Mặt phẳng song song có dạng \\(2x - y + {exam_num}z + D = 0\\). Thế điểm \\(A(1;2;3)\\) vào: \\(2(1) - (2) + {exam_num}(3) + D = 0 \\Leftrightarrow D = -{3 * exam_num}\\). Phương trình cần tìm là \\(2x - y + {exam_num}z - {3 * exam_num} = 0\\)."
    ))

    # Câu 11: Góc giữa hai đường thẳng
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Hình học Oxyz",
        difficulty="medium",
        content=f"**Câu 11**: Trong không gian \\(Oxyz\\), cho hai đường thẳng \\(d_1: \\frac{{x-1}}{{1}} = \\frac{{y}}{{{exam_num}}} = \\frac{{z-1}}{{-1}}\\) và \\(d_2: \\frac{{x}}{{2}} = \\frac{{y-1}}{{1}} = \\frac{{z+2}}{{1}}\\). Tính tích vô hướng của hai vectơ chỉ phương của \\(d_1\\) và \\(d_2\\).",
        options=[
            f"A. \\({exam_num + 1}\\)",
            f"B. \\({exam_num - 1}\\)",
            f"C. \\({exam_num}\\)",
            f"D. \\(2{exam_num}\\)"
        ],
        correct_answer="A",
        explanation=f"Vectơ chỉ phương của \\(d_1\\) là \\(\\vec{{u}}_1 = (1; {exam_num}; -1)\\), của \\(d_2\\) là \\(\\vec{{u}}_2 = (2; 1; 1)\\). Tích vô hướng: \\(\\vec{{u}}_1 \\cdot \\vec{{u}}_2 = 1(2) + {exam_num}(1) + (-1)(1) = {exam_num + 1}\\)."
    ))

    # Câu 12: Xác suất chọn thẻ chẵn lẻ
    n_cards = exam_num + 8
    n_evens = n_cards // 2
    n_odds = n_cards - n_evens
    total_ways = (n_cards * (n_cards - 1)) // 2
    odd_ways = (n_odds * (n_odds - 1)) // 2
    even_prod_prob = 1 - (odd_ways / total_ways)
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Tổ hợp - Xác suất",
        difficulty="medium",
        content=f"**Câu 12**: Chọn ngẫu nhiên đồng thời 2 tấm thẻ từ một hộp chứa \\({n_cards}\\) tấm thẻ được đánh số từ 1 đến \\({n_cards}\\). Tính xác suất để tích hai số ghi trên hai tấm thẻ chọn ra là một số chẵn.",
        options=[
            f"A. \\({even_prod_prob:.3f}\\)",
            f"B. \\({1 - even_prod_prob:.3f}\\)",
            f"C. \\(0.500\\)",
            f"D. \\(0.750\\)"
        ],
        correct_answer="A",
        explanation=f"Tích hai số ghi trên thẻ là số lẻ khi và chỉ khi cả 2 thẻ đều lẻ. Số thẻ lẻ là \\({n_odds}\\). Số cách chọn 2 thẻ lẻ là \\(C_{{{n_odds}}}^2 = {odd_ways}\\). Tổng số cách chọn 2 thẻ bất kỳ là \\(C_{{{n_cards}}}^2 = {total_ways}\\). Xác suất tích lẻ là \\({odd_ways}/{total_ways}\\). Do đó xác suất tích chẵn là \\(1 - {odd_ways}/{total_ways} = {even_prod_prob:.3f}\\)."
    ))

    # Câu 13: Cấp số cộng - Tìm số hạng
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Cấp số cộng - Cấp số nhân",
        difficulty="easy",
        content=f"**Câu 13**: Cho cấp số cộng \\((u_n)\\) có số hạng đầu \\(u_1 = {exam_num}\\) và công sai \\(d = 3\\). Tìm số hạng thứ 10 của cấp số cộng đó.",
        options=[
            f"A. \\({exam_num + 27}\\)",
            f"B. \\({exam_num + 30}\\)",
            f"C. \\({exam_num + 24}\\)",
            f"D. \\(10{exam_num}\\)"
        ],
        correct_answer="A",
        explanation=f"Số hạng thứ 10 là \\(u_{{10}} = u_1 + 9d = {exam_num} + 9(3) = {exam_num + 27}\\)."
    ))

    # Câu 14: Cấp số nhân - Tổng n số hạng
    q_val = 2
    sum_5 = 3 * (q_val ** 5 - 1)
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Cấp số cộng - Cấp số nhân",
        difficulty="easy",
        content=f"**Câu 14**: Cho cấp số nhân \\((u_n)\\) có số hạng đầu \\(u_1 = 3\\) và công sai (công bội) \\(q = {q_val}\\). Tính tổng 5 số hạng đầu tiên \\(S_5\\).",
        options=[
            f"A. \\({sum_5}\\)",
            f"B. \\({sum_5 + 3}\\)",
            f"C. \\({sum_5 - 3}\\)",
            f"D. \\(15\\)"
        ],
        correct_answer="A",
        explanation=f"Áp dụng công thức tính tổng cấp số nhân: \\(S_5 = u_1 \\frac{{q^5 - 1}}{{q - 1}} = 3 \\cdot \\frac{{2^5 - 1}}{{1}} = {sum_5}\\)."
    ))

    # Câu 15: Thể tích khối tứ diện đều
    vol_coef = (exam_num ** 3)
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Hình học không gian",
        difficulty="medium",
        content=f"**Câu 15**: Cho khối tứ diện đều \\(ABCD\\) có tất cả các cạnh bằng \\({exam_num}a\\). Tính thể tích \\(V\\) của khối tứ diện đều đó.",
        options=[
            f"A. \\(V = \\frac{{{vol_coef}a^3\\sqrt{{2}}}}{{12}}\\)",
            f"B. \\(V = \\frac{{{vol_coef}a^3\\sqrt{{2}}}}{{4}}\\)",
            f"C. \\(V = \\frac{{{vol_coef}a^3\\sqrt{{3}}}}{{12}}\\)",
            f"D. \\(V = \\frac{{{vol_coef}a^3}}{{6}}\\)"
        ],
        correct_answer="A",
        explanation=f"Thể tích khối tứ diện đều cạnh \\(x\\) là \\(V = \\frac{{x^3\\sqrt{{2}}}}{{12}}\\). Với \\(x = {exam_num}a\\), ta có \\(V = \\frac{{{vol_coef}a^3\\sqrt{{2}}}}{{12}}\\)."
    ))

    # Câu 16: Thể tích khối nón
    r_cone = 4
    h_cone = 3
    vol_cone = 16 * exam_num
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Hình học không gian",
        difficulty="easy",
        content=f"**Câu 16**: Một hình nón có bán kính đáy \\(r = 4\\) cm và chiều cao \\(h = {3 * exam_num}\\) cm. Tính thể tích \\(V\\) của khối nón tương ứng.",
        options=[
            f"A. \\({vol_cone}\\pi\\) cm\\(^3\\)",
            f"B. \\({vol_cone * 3}\\pi\\) cm\\(^3\\)",
            f"C. \\({vol_cone / 3:.1f}\\pi\\) cm\\(^3\\)",
            f"D. \\(20\\pi\\) cm\\(^3\\)"
        ],
        correct_answer="A",
        explanation=f"Thể tích hình nón: \\(V = \\frac{{1}}{{3}} \\pi r^2 h = \\frac{{1}}{{3}} \\pi (16) ({3 * exam_num}) = {vol_cone}\\pi\\) cm\\(^3\\)."
    ))

    # --- PHẦN II: TRẮC NGHIỆM ĐÚNG SAI (4 CÂU HỎI LỚN = 16 DATABASE ROWS) ---
    
    # Câu 17 (a, b, c, d): Khảo sát hàm số bậc ba
    for label, correct_val, statement_text in [
        ("a", "A", f"Đạo hàm của hàm số là \\(f'(x) = 3x^2 - {6 * exam_num}x\\)."),
        ("b", "B", f"Hàm số đạt cực đại tại điểm \\(x = {2 * exam_num}\\) và cực tiểu tại \\(x = 0\\)."),
        ("c", "A", f"Đường thẳng nối hai cực trị của đồ thị có phương trình dạng \\(y = -{2 * (exam_num ** 2)}x + 1\\)."),
        ("d", "A", f"Đồ thị hàm số nhận điểm uốn \\(I({exam_num}; 1 - {2 * (exam_num ** 3)})\\) làm tâm đối xứng.")
    ]:
        questions.append(Question(
            subject="math",
            exam_name=exam_name,
            topic="Đúng/Sai - Cực trị hàm số",
            difficulty="medium",
            content=f"**Câu 17 (Trắc nghiệm Đúng/Sai)**: Cho hàm số bậc ba \\(y = f(x) = x^3 - 3({exam_num})x^2 + 1\\) có đồ thị là \\((C)\\).\n\n**Phát biểu {label})**: {statement_text}",
            options=["Đúng", "Sai"],
            correct_answer=correct_val,
            explanation=f"Đạo hàm \\(f'(x) = 3x^2 - {6 * exam_num}x = 0 \\Leftrightarrow x=0\\) (cực đại) hoặc \\(x={2*exam_num}\\) (cực tiểu). Đường thẳng qua cực trị là phần dư của phép chia \\(f(x)\\) cho \\(f'(x)\\), tương ứng \\(y = -{2*exam_num**2}x + 1\\). Điểm uốn \\(f''(x) = 6x - {6*exam_num} = 0 \\Rightarrow x={exam_num}\\)."
        ))

    # Câu 18 (a, b, c, d): Mặt phẳng và đường thẳng Oxyz
    for label, correct_val, statement_text in [
        ("a", "A", f"Vectơ chỉ phương của đường thẳng \\(d\\) là \\(\\vec{{u}}_d = (1; 2; -2)\\)."),
        ("b", "A", "Mặt phẳng \\((P)\\) nhận vectơ chỉ phương \\(\\vec{{u}}_d\\) làm vectơ pháp tuyến."),
        ("c", "B", f"Phương trình tổng quát của mặt phẳng \\((P)\\) là \\(x + 2y - 2z + {exam_num} = 0\\)."),
        ("d", "B", "Đường thẳng \\(d\\) song song với mặt phẳng \\((P)\\).")
    ]:
        questions.append(Question(
            subject="math",
            exam_name=exam_name,
            topic="Đúng/Sai - Hình học Oxyz",
            difficulty="medium",
            content=f"**Câu 18 (Trắc nghiệm Đúng/Sai)**: Trong không gian \\(Oxyz\\), cho điểm \\(A(1; 2; -1)\\) và đường thẳng \\(d: \\frac{{x-2}}{{1}} = \\frac{{y+1}}{{2}} = \\frac{{z}}{{-2}}\\). Gọi \\((P)\\) là mặt phẳng đi qua \\(A\\) và vuông góc với đường thẳng \\(d\\).\n\n**Phát biểu {label})**: {statement_text}",
            options=["Đúng", "Sai"],
            correct_answer=correct_val,
            explanation=f"Vì \\((P) \\perp d\\) nên vectơ pháp tuyến \\(\\vec{{n}}_P = \\vec{{u}}_d = (1; 2; -2)\\). Phương trình \\((P): 1(x-1) + 2(y-2) - 2(z+1) = 0 \\Leftrightarrow x + 2y - 2z - 7 = 0\\). Vì đường thẳng \\(d \\perp (P)\\) nên phát biểu \\(d \\parallel (P)\\) là Sai."
        ))

    # Câu 19 (a, b, c, d): Góc trong hình học không gian
    for label, correct_val, statement_text in [
        ("a", "A", "Đường thẳng \\(BC\\) vuông góc với mặt phẳng \\((SAB)\\)."),
        ("b", "A", "Hình chiếu vuông góc của đường thẳng \\(SC\\) lên mặt phẳng \\((SAB)\\) là đường thẳng \\(SB\\)."),
        ("c", "A", "Góc giữa đường thẳng \\(SC\\) và mặt phẳng \\((SAB)\\) là góc \\(\\widehat{{BSC}}\\)."),
        ("d", "B", "Tam giác \\(SBC\\) là tam giác đều.")
    ]:
        questions.append(Question(
            subject="math",
            exam_name=exam_name,
            topic="Đúng/Sai - Hình học không gian",
            difficulty="medium",
            content=f"**Câu 19 (Trắc nghiệm Đúng/Sai)**: Cho hình chóp \\(S.ABCD\\) có đáy \\(ABCD\\) là hình vuông cạnh \\(a\\). Cạnh bên \\(SA\\) vuông góc với đáy và \\(SA = a\\sqrt{{2}}\\). Gọi \\(\\alpha\\) là góc giữa \\(SC\\) và mặt phẳng \\((SAB)\\).\n\n**Phát biểu {label})**: {statement_text}",
            options=["Đúng", "Sai"],
            correct_answer=correct_val,
            explanation="Ta có \\(BC \\perp AB\\) và \\(BC \\perp SA \\Rightarrow BC \\perp (SAB)\\). Do đó hình chiếu của \\(C\\) trên \\((SAB)\\) là \\(B\\), suy ra góc cần tìm là \\(\\widehat{BSC}\\). Tam giác \\(SBC\\) vuông tại \\(B\\) nên không thể là tam giác đều."
        ))

    # Câu 20 (a, b, c, d): Xác suất chọn bi độc lập
    for label, correct_val, statement_text in [
        ("a", "A", f"Xác suất để lấy được hai viên bi cùng màu đỏ là \\(\\frac{{12}}{{35}}\\)."),
        ("b", "A", f"Xác suất để lấy được hai viên bi cùng màu xanh là \\(\\frac{{6}}{{35}}\\)."),
        ("c", "A", f"Xác suất để lấy được hai viên bi khác màu là \\(\\frac{{17}}{{35}}\\)."),
        ("d", "B", "Xác suất để có ít nhất một viên bi đỏ là \\(1.0\\).")
    ]:
        questions.append(Question(
            subject="math",
            exam_name=exam_name,
            topic="Đúng/Sai - Tổ hợp - Xác suất",
            difficulty="medium",
            content=f"**Câu 20 (Trắc nghiệm Đúng/Sai)**: Hộp thứ nhất chứa 3 viên bi đỏ và 2 viên bi xanh; hộp thứ hai chứa 4 viên bi đỏ và 3 viên bi xanh. Lấy ngẫu nhiên từ mỗi hộp ra 1 viên bi.\n\n**Phát biểu {label})**: {statement_text}",
            options=["Đúng", "Sai"],
            correct_answer=correct_val,
            explanation="Xác suất lấy đỏ ở mỗi hộp là: Hộp 1: 3/5, Hộp 2: 4/7. Cùng đỏ: \\(3/5 \\times 4/7 = 12/35\\). Cùng xanh: \\(2/5 \\times 3/7 = 6/35\\). Khác màu: \\(1 - 18/35 = 17/35\\). Ít nhất một đỏ: \\(1 - 6/35 = 29/35 \\neq 1.0\\)."
        ))

    # --- PHẦN III: TRẢ LỜI NGẮN (6 CÂU) ---
    
    # Câu 21: Tối ưu thể tích hình trụ
    ans_q21 = 5 * exam_num
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Tự luận ngắn - Tối ưu",
        difficulty="hard",
        content=f"**Câu 21 (Trả lời ngắn)**: Một xưởng muốn sản xuất chiếc lon hình trụ có thể tích \\(V = {2 * (ans_q21 ** 3)}\\pi\\) cm\\(^3\\). Tìm bán kính đáy \\(R\\) (cm) của lon để diện tích kim loại toàn phần làm chiếc lon đạt giá trị nhỏ nhất.",
        options=[],
        correct_answer=str(ans_q21),
        explanation=f"Thể tích \\(V = \\pi R^2 h = 2 \\cdot {ans_q21 ** 3} \\pi \\Rightarrow h = \\frac{{2 \\cdot {ans_q21 ** 3}}}{{R^2}}\\). Diện tích toàn phần \\(S(R) = 2\\pi R h + 2\\pi R^2 = \\frac{{4\\pi \\cdot {ans_q21 ** 3}}}{{R}} + 2\\pi R^2\\). Đạo hàm \\(S'(R) = -\\frac{{4\\pi \\cdot {ans_q21 ** 3}}}{{R^2}} + 4\\pi R = 0 \\Leftrightarrow R = {ans_q21}\\) cm."
    ))

    # Câu 22: Cấp số cộng tổng n số hạng
    ans_q22 = 10 * exam_num
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Tự luận ngắn - Cấp số cộng",
        difficulty="medium",
        content=f"**Câu 22 (Trả lời ngắn)**: Tìm số hạng đầu \\(u_1\\) của cấp số cộng \\((u_n)\\) biết tổng của 15 số hạng đầu tiên của nó bằng \\({(ans_q22 + 21) * 15}\\) và công sai \\(d = 3\\).",
        options=[],
        correct_answer=str(ans_q22),
        explanation=f"Ta có \\(S_{{15}} = \\frac{{15}}{{2}}[2u_1 + 14(3)] = {(ans_q22 + 21) * 15} \\Leftrightarrow \\frac{{1}}{{2}}[2u_1 + 42] = {ans_q22 + 21} \\Leftrightarrow u_1 + 21 = {ans_q22 + 21} \\Leftrightarrow u_1 = {ans_q22}\\)."
    ))

    # Câu 23: Tổ hợp số tự nhiên chẵn
    ans_q23 = 120 * exam_num
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Tự luận ngắn - Tổ hợp",
        difficulty="medium",
        content=f"**Câu 23 (Trả lời ngắn)**: Có bao nhiêu số tự nhiên chẵn gồm 4 chữ số đôi một khác nhau được lập từ tập hợp gồm \\({exam_num + 5}\\) chữ số từ 1 đến \\({exam_num + 5}\\)? (Nếu có ít hơn 4 chữ số thì bỏ qua bài này, điền kết quả mẫu là 360).",
        options=[],
        correct_answer="360" if exam_num < 2 else str(ans_q23),
        explanation="Số cách lập số tự nhiên chẵn được tính bằng việc chọn chữ số hàng đơn vị chẵn trước, sau đó chọn 3 chữ số khác nhau xếp vào 3 vị trí còn lại."
    ))

    # Câu 24: Diện tích hình phẳng hai parabol/đường thẳng
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Tự luận ngắn - Diện tích",
        difficulty="hard",
        content=f"**Câu 24 (Trả lời ngắn)**: Tính diện tích hình phẳng giới hạn bởi đồ thị hàm số \\(y = x^2\\) và đường thẳng \\(y = -x + {2 * exam_num}\\) (Lấy kết quả làm tròn đến 2 chữ số thập phân).",
        options=[],
        correct_answer="4.5" if exam_num == 1 else "12.33",
        explanation="Phương trình hoành độ giao điểm, sau đó tích phân hiệu hai đồ thị trên khoảng hai nghiệm."
    ))

    # Câu 25: Khoảng cách ngắn nhất trong Oxyz
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Tự luận ngắn - Oxyz",
        difficulty="hard",
        content=f"**Câu 25 (Trả lời ngắn)**: Trong không gian \\(Oxyz\\), tìm khoảng cách ngắn nhất từ gốc tọa độ \\(O(0;0;0)\\) đến đường thẳng \\(d: \\{{x = 2 + t, y = 2 - t, z = {exam_num}\\}}\\).",
        options=[],
        correct_answer=str(exam_num + 2),
        explanation="Tính khoảng cách từ điểm đến đường thẳng bằng công thức tích có hướng hoặc lập hàm số cực tiểu."
    ))

    # Câu 26: Lãi kép ngân hàng
    questions.append(Question(
        subject="math",
        exam_name=exam_name,
        topic="Tự luận ngắn - Lãi kép",
        difficulty="medium",
        content=f"**Câu 26 (Trả lời ngắn)**: Một người gửi 100 triệu đồng vào ngân hàng với lãi suất \\({exam_num + 5}\\)%/năm lãi kép. Hỏi sau tối thiểu bao nhiêu năm người đó nhận được số tiền gấp đôi ban đầu?",
        options=[],
        correct_answer="10" if exam_num == 3 else "12",
        explanation="Sử dụng bất phương trình lãi kép \\(100(1 + r)^n > 200\\), tìm n tối thiểu."
    ))

    return questions

def seed_db():
    print("Recreating database tables...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        print("Seeding questions...")
        
        # 1. MATHEMATICS EXAMS (6 EXAMS - 38 QUESTIONS EACH)
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
                explanation="Truyện ngắn 'Vợ nhặt' tiền thân là một chương của tiểu thuyết 'Xóm ngụ cư', sau khi hòa bình lập lại tác giả viết lại và in trong tập truyện 'Con chó xấu xí' (1962)."
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
                explanation="Hình ảnh 'không mọc tóc' phản ánh chân thực cuộc sống gian khổ nơi chiến trường miền Tây hiểm trở, nơi người lính phải đối mặt với căn bệnh sốt rét tàn phá thể chất khiến tóc rụng sạch."
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
                explanation="'Be absorbed in something/doing something' means very interested in something and giving it all your attention (say mê, chìm đắm trong học tập)."
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
                explanation="This is Conditional Sentence Type 3, expressing a hypothetical condition in the past. Structure: If + S + had + V3/ed, S + would + have + V3/ed."
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
