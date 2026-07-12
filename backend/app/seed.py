import sys
import os
import json

# Add the parent directory to python path to import app correctly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.core.database import SessionLocal, Base, engine
from app.models.question import Question

def get_default_exams_json():
    exams = []
    for exam_num in range(1, 7):
        y_cd = 2
        y_ct = 2 - 4 * (exam_num ** 3)
        base_val = exam_num + 2
        x_val = exam_num + 1
        ans_q4 = exam_num + 4
        n_cards = exam_num + 8
        n_evens = n_cards // 2
        n_odds = n_cards - n_evens
        total_ways = (n_cards * (n_cards - 1)) // 2
        odd_ways = (n_odds * (n_odds - 1)) // 2
        even_prod_prob = round(1 - (odd_ways / total_ways), 3)
        vol_coef = (exam_num ** 3)
        vol_cone = 16 * exam_num
        ans_q21 = 5 * exam_num
        ans_q22 = 10 * exam_num
        ans_q23 = 120 * exam_num
        q_val = 2
        sum_5 = 3 * (q_val ** 5 - 1)

        exam = {
            "exam_title": f"Đề số {exam_num}",
            "duration_minutes": 90,
            "sections": [
                {
                    "section_id": 1,
                    "section_title": "PHẦN I. TRẮC NGHIỆM KHÁCH QUAN",
                    "questions": [
                        {
                            "question_number": 1,
                            "question_text": f"Cho hàm số $y = f(x) = x^3 - 3({exam_num})x^2 + 2$ liên tục trên $\\mathbb{{R}}$. Tìm tập hợp tất cả các giá trị của tham số $m$ để phương trình $f(x) = m$ có đúng 3 nghiệm thực phân biệt.",
                            "choices": {
                                "A": f"${y_ct} < m < {y_cd}$",
                                "B": f"$m > {y_cd}$",
                                "C": f"$m < {y_ct}$",
                                "D": f"$m = {y_cd}$ hoặc $m = {y_ct}$"
                            },
                            "correct_answer": "A",
                            "explanation": f"Đạo hàm $y' = 3x^2 - 6({exam_num})x = 3x(x - {2 * exam_num})$. Cho $y' = 0 \\Leftrightarrow x = 0$ hoặc $x = {2 * exam_num}$. Đồ thị có điểm cực đại là $(0; 2)$ và điểm cực tiểu là $({2 * exam_num}; {y_ct})$. Phương trình có 3 nghiệm phân biệt khi đường thẳng $y = m$ cắt đồ thị tại 3 điểm phân biệt, tương đương ${y_ct} < m < {y_cd}$."
                        },
                        {
                            "question_number": 2,
                            "question_text": f"Tính đạo hàm của hàm số $y = {base_val}^{{x^2 - 2x}}$.",
                            "choices": {
                                "A": f"$y' = (2x - 2) \\cdot {base_val}^{{x^2 - 2x}} \\cdot \\ln {base_val}$",
                                "B": f"$y' = (x^2 - 2x) \\cdot {base_val}^{{x^2 - 2x - 1}}$",
                                "C": f"$y' = {base_val}^{{x^2 - 2x}} \\cdot \\ln {base_val}$",
                                "D": f"$y' = \\frac{{2x - 2}}{{\\ln {base_val}}} \\cdot {base_val}^{{x^2 - 2x}}$"
                            },
                            "correct_answer": "A",
                            "explanation": f"Áp dụng công thức đạo hàm hàm hợp $(a^u)' = u' \\cdot a^u \\cdot \\ln a$. Ở đây $a = {base_val}$, $u = x^2 - 2x \\Rightarrow u' = 2x - 2$. Do đó ta có: $y' = (2x - 2) \\cdot {base_val}^{{x^2 - 2x}} \\cdot \\ln {base_val}$."
                        },
                        {
                            "question_number": 3,
                            "question_text": f"Tìm tập xác định $D$ của hàm số $y = (x^2 - {exam_num + 2}x + {exam_num + 1})^{{-e}}$.",
                            "choices": {
                                "A": f"$D = (-\\infty; 1) \\cup ({x_val}; +\\infty)$",
                                "B": f"$D = \\mathbb{{R}} \\setminus \\{{1; {x_val}\\}}$",
                                "C": f"$D = (1; {x_val})$",
                                "D": f"$D = \\mathbb{{R}}$"
                            },
                            "correct_answer": "A",
                            "explanation": f"Hàm số lũy thừa có số mũ không nguyên xác định khi cơ số dương: $x^2 - {exam_num + 2}x + {exam_num + 1} > 0 \\Leftrightarrow (x-1)(x-{x_val}) > 0 \\Leftrightarrow x < 1$ hoặc $x > {x_val}$. Tập xác định là $D = (-\\infty; 1) \\cup ({x_val}; +\\infty)$."
                        },
                        {
                            "question_number": 4,
                            "question_text": f"Giải phương trình $\\log_2(x - {exam_num + 2}) + \\log_2(x - {exam_num}) = 3$.",
                            "choices": {
                                "A": f"$x = {ans_q4}$",
                                "B": f"$x = {ans_q4}$ hoặc $x = {exam_num - 2}$",
                                "C": f"$x = {ans_q4 - 1}$",
                                "D": f"$x = {exam_num + 2}$"
                            },
                            "correct_answer": "A",
                            "explanation": f"Điều kiện: $x > {exam_num + 2}$. Phương trình viết lại: $\\log_2[(x - {exam_num + 2})(x - {exam_num})] = 3 \\Leftrightarrow x^2 - {2 * exam_num + 2}x + {exam_num * (exam_num + 2)} = 8 \\Leftrightarrow x^2 - {2 * exam_num + 2}x + {exam_num ** 2 + 2 * exam_num - 8} = 0 \\Leftrightarrow x = {ans_q4}$ (nhận) hoặc $x = {exam_num - 2}$ (loại do điều kiện)."
                        },
                        {
                            "question_number": 5,
                            "question_text": f"Tìm nguyên hàm $F(x)$ của hàm số $f(x) = \\frac{{2x + {exam_num + 2}}}{{x + 1}}$ trên khoảng $(-1; +\\infty)$ biết $F(0) = 2$.",
                            "choices": {
                                "A": f"$F(x) = 2x + {exam_num}\\ln(x + 1) + 2$",
                                "B": f"$F(x) = 2x + {exam_num}\\ln|x + 1| + C$",
                                "C": f"$F(x) = 2x - {exam_num}\\ln(x + 1) + 2$",
                                "D": f"$F(x) = 2x + {exam_num + 2}\\ln(x + 1) + 2$"
                            },
                            "correct_answer": "A",
                            "explanation": f"Ta có $f(x) = \\frac{{2(x+1) + {exam_num}}}{{x+1}} = 2 + \\frac{{{exam_num}}}{{x+1}}$. Nguyên hàm là $F(x) = 2x + {exam_num}\\ln(x+1) + C$ (vì $x > -1$). Từ $F(0) = 2 \\Rightarrow 0 + 0 + C = 2 \\Rightarrow C = 2$. Vậy $F(x) = 2x + {exam_num}\\ln(x+1) + 2$."
                        },
                        {
                            "question_number": 6,
                            "question_text": f"Tính diện tích $S$ của hình phẳng giới hạn bởi đồ thị hàm số $y = x^3 - {exam_num ** 2}x$ và trục hoành $Ox$.",
                            "choices": {
                                "A": f"$S = \\frac{{{exam_num ** 4}}}{{2}}$",
                                "B": f"$S = \\frac{{{exam_num ** 4}}}{{4}}$",
                                "C": f"$S = {exam_num ** 4}$",
                                "D": f"$S = 2({exam_num ** 4})$"
                            },
                            "correct_answer": "A",
                            "explanation": f"Phương trình hoành độ giao điểm: $x^3 - {exam_num ** 2}x = 0 \\Leftrightarrow x = 0, x = \\pm {exam_num}$. Do đồ thị đối xứng qua gốc tọa độ: $S = 2 \\int_{{0}}^{{{exam_num}}} |x^3 - {exam_num ** 2}x| dx = 2 \\int_{{0}}^{{{exam_num}}} ({exam_num ** 2}x - x^3) dx = 2 \\left. \\left( \\frac{{{exam_num ** 2}x^2}}{{2}} - \\frac{{x^4}}{{4}} \\right) \\right|_{{0}}^{{{exam_num}}} = 2 \\left( \\frac{{{exam_num ** 4}}}{{2}} - \\frac{{{exam_num ** 4}}}{{4}} \\right) = \\frac{{{exam_num ** 4}}}{{2}}$."
                        },
                        {
                            "question_number": 7,
                            "question_text": f"Tìm số phức liên hợp $\\overline{{z}}$ của số phức $z$ thỏa mãn $(1 + i)z = {exam_num + 2} - i$.",
                            "choices": {
                                "A": f"$\\overline{{z}} = \\frac{{{exam_num + 1}}}{{2}} + \\frac{{{exam_num + 3}}}{{2}}i$",
                                "B": f"$\\overline{{z}} = \\frac{{{exam_num + 1}}}{{2}} - \\frac{{{exam_num + 3}}}{{2}}i$",
                                "C": f"$\\overline{{z}} = \\frac{{{exam_num + 3}}}{{2}} + \\frac{{{exam_num + 1}}}{{2}}i$",
                                "D": f"$\\overline{{z}} = -\\frac{{{exam_num + 1}}}{{2}} - \\frac{{{exam_num + 3}}}{{2}}i$"
                            },
                            "correct_answer": "A",
                            "explanation": f"Ta có $z = \\frac{{{exam_num + 2} - i}}{{1 + i}} = \\frac{{({exam_num + 2} - i)(1 - i)}}{{2}} = \\frac{{{exam_num + 1} - ({exam_num + 3})i}}{{2}}$. Suy ra số phức liên hợp là $\\overline{{z}} = \\frac{{{exam_num + 1}}}{{2}} + \\frac{{{exam_num + 3}}}{{2}}i$."
                        },
                        {
                            "question_number": 8,
                            "question_text": f"Tính môđun của số phức $z = {exam_num} + 4i$.",
                            "choices": {
                                "A": f"$|z| = \\sqrt{{{exam_num ** 2 + 16}}}$",
                                "B": f"$|z| = {exam_num ** 2 + 16}$",
                                "C": f"$|z| = {exam_num + 4}$",
                                "D": f"$|z| = \\sqrt{{{exam_num ** 2 - 16}}}$"
                            },
                            "correct_answer": "A",
                            "explanation": f"Áp dụng công thức tính môđun của số phức $z = a + bi$: $|z| = \\sqrt{{a^2 + b^2}} = \\sqrt{{{exam_num}^2 + 4^2}} = \\sqrt{{{exam_num ** 2 + 16}}}$."
                        },
                        {
                            "question_number": 9,
                            "question_text": f"Trong không gian $Oxyz$, cho hai điểm $A({exam_num}; 2; -3)$ và $B(3; 0; -1)$. Tìm tọa độ trung điểm $M$ của đoạn thẳng $AB$.",
                            "choices": {
                                "A": f"$M\\left(\\frac{{{exam_num + 3}}}{{2}}; 1; -2\\right)$",
                                "B": f"$M({exam_num + 3}; 2; -4)$",
                                "C": f"$M\\left(\\frac{{{exam_num - 3}}}{{2}}; 1; -1\\right)$",
                                "D": f"$M\\left(\\frac{{{exam_num + 3}}}{{2}}; 1; -1\\right)$"
                            },
                            "correct_answer": "A",
                            "explanation": f"Áp dụng công thức trung điểm: $x_M = \\frac{{x_A + x_B}}{{2}} = \\frac{{{exam_num} + 3}}{{2}}$; $y_M = 1$; $z_M = -2$. Tọa độ trung điểm là $M\\left(\\frac{{{exam_num + 3}}}{{2}}; 1; -2\\right)$."
                        },
                        {
                            "question_number": 10,
                            "question_text": f"Trong không gian $Oxyz$, viết phương trình mặt phẳng đi qua điểm $A(1; 2; 3)$ và song song với mặt phẳng $(P): 2x - y + {exam_num}z - 5 = 0$.",
                            "choices": {
                                "A": f"$2x - y + {exam_num}z - {3 * exam_num} = 0$",
                                "B": f"$2x - y + {exam_num}z + {3 * exam_num} = 0$",
                                "C": f"$2x - y + {exam_num}z - 5 = 0$",
                                "D": f"$2x - y + {exam_num}z = 0$"
                            },
                            "correct_answer": "A",
                            "explanation": f"Mặt phẳng song song có dạng $2x - y + {exam_num}z + D = 0$. Thế điểm $A(1;2;3)$ vào: $2(1) - (2) + {exam_num}(3) + D = 0 \\Leftrightarrow D = -{3 * exam_num}$. Phương trình cần tìm là $2x - y + {exam_num}z - {3 * exam_num} = 0$."
                        },
                        {
                            "question_number": 11,
                            "question_text": f"Trong không gian $Oxyz$, cho hai đường thẳng $d_1: \\frac{{x-1}}{{1}} = \\frac{{y}}{{{exam_num}}} = \\frac{{z-1}}{{-1}}$ và $d_2: \\frac{{x}}{{2}} = \\frac{{y-1}}{{1}} = \\frac{{z+2}}{{1}}$. Tính tích vô hướng của hai vectơ chỉ phương của $d_1$ và $d_2$.",
                            "choices": {
                                "A": f"${exam_num + 1}$",
                                "B": f"${exam_num - 1}$",
                                "C": f"${exam_num}$",
                                "D": f"$2{exam_num}$"
                            },
                            "correct_answer": "A",
                            "explanation": f"Vectơ chỉ phương của $d_1$ là $\\vec{{u}}_1 = (1; {exam_num}; -1)$, của $d_2$ là $\\vec{{u}}_2 = (2; 1; 1)$. Tích vô hướng: $\\vec{{u}}_1 \\cdot \\vec{{u}}_2 = 1(2) + {exam_num}(1) + (-1)(1) = {exam_num + 1}$."
                        },
                        {
                            "question_number": 12,
                            "question_text": f"Chọn ngẫu nhiên đồng thời 2 tấm thẻ từ một hộp chứa {n_cards} tấm thẻ được đánh số từ 1 đến {n_cards}. Tính xác suất để tích hai số ghi trên hai tấm thẻ chọn ra là một số chẵn.",
                            "choices": {
                                "A": f"${even_prod_prob}$",
                                "B": f"${round(1 - even_prod_prob, 3)}$",
                                "C": "$0.5$",
                                "D": "$0.75$"
                            },
                            "correct_answer": "A",
                            "explanation": f"Tích hai số ghi trên thẻ là số lẻ khi và chỉ khi cả 2 thẻ đều lẻ. Số thẻ lẻ là {n_odds}. Số cách chọn 2 thẻ lẻ là $C_{{{n_odds}}}^2 = {odd_ways}$. Tổng số cách chọn 2 thẻ bất kỳ là $C_{{{n_cards}}}^2 = {total_ways}$. Xác suất tích lẻ là {odd_ways}/{total_ways}. Do đó xác suất tích chẵn là $1 - {odd_ways}/{total_ways} = {even_prod_prob}$."
                        },
                        {
                            "question_number": 13,
                            "question_text": f"Cho cấp số cộng $(u_n)$ có số hạng đầu $u_1 = {exam_num}$ và công sai $d = 3$. Tìm số hạng thứ 10 của cấp số cộng đó.",
                            "choices": {
                                "A": f"${exam_num + 27}$",
                                "B": f"${exam_num + 30}$",
                                "C": f"${exam_num + 24}$",
                                "D": f"$10{exam_num}$"
                            },
                            "correct_answer": "A",
                            "explanation": f"Số hạng thứ 10 là $u_{{10}} = u_1 + 9d = {exam_num} + 9(3) = {exam_num + 27}$."
                        },
                        {
                            "question_number": 14,
                            "question_text": f"Cho cấp số nhân $(u_n)$ có số hạng đầu $u_1 = 3$ và công sai (công bội) $q = 2$. Tính tổng 5 số hạng đầu tiên $S_5$.",
                            "choices": {
                                "A": f"${sum_5}$",
                                "B": f"${sum_5 + 3}$",
                                "C": f"${sum_5 - 3}$",
                                "D": "$15$"
                            },
                            "correct_answer": "A",
                            "explanation": f"Áp dụng công thức tính tổng cấp số nhân: $S_5 = u_1 \\frac{{q^5 - 1}}{{q - 1}} = 3 \\cdot \\frac{{2^5 - 1}}{{1}} = {sum_5}$."
                        },
                        {
                            "question_number": 15,
                            "question_text": f"Cho khối tứ diện đều $ABCD$ có tất cả các cạnh bằng ${exam_num}a$. Tính thể tích $V$ của khối tứ diện đều đó.",
                            "choices": {
                                "A": f"$V = \\frac{{{vol_coef}a^3\\sqrt{{2}}}}{{12}}$",
                                "B": f"$V = \\frac{{{vol_coef}a^3\\sqrt{{2}}}}{{4}}$",
                                "C": f"$V = \\frac{{{vol_coef}a^3\\sqrt{{3}}}}{{12}}$",
                                "D": f"$V = \\frac{{{vol_coef}a^3}}{{6}}$"
                            },
                            "correct_answer": "A",
                            "explanation": f"Thể tích khối tứ diện đều cạnh $x$ là $V = \\frac{{x^3\\sqrt{{2}}}}{{12}}$. Với $x = {exam_num}a$, ta có $V = \\frac{{{vol_coef}a^3\\sqrt{{2}}}}{{12}}$."
                        },
                        {
                            "question_number": 16,
                            "question_text": f"Một hình nón có bán kính đáy $r = 4$ cm và chiều cao $h = {3 * exam_num}$ cm. Tính thể tích $V$ của khối nón tương ứng.",
                            "choices": {
                                "A": f"${vol_cone}\\pi$ cm$^3$",
                                "B": f"${vol_cone * 3}\\pi$ cm$^3$",
                                "C": f"${vol_cone / 3:.1f}\\pi$ cm$^3$",
                                "D": "$20\\pi$ cm$^3$"
                            },
                            "correct_answer": "A",
                            "explanation": f"Thể tích hình nón: $V = \\frac{{1}}{{3}} \\pi r^2 h = \\frac{{1}}{{3}} \\pi (16) ({3 * exam_num}) = {vol_cone}\\pi$ cm$^3$."
                        }
                    ]
                },
                {
                    "section_id": 2,
                    "section_title": "PHẦN II. TRĂC NGHIỆM ĐÚNG SAI",
                    "questions": [
                        {
                            "question_number": 1,
                            "context_text": f"Cho hàm số bậc ba $y = f(x) = x^3 - 3({exam_num})x^2 + 1$ có đồ thị là $(C)$.",
                            "statements": [
                                {
                                    "label": "a",
                                    "text": f"Đạo hàm của hàm số là $f'(x) = 3x^2 - {6 * exam_num}x$.",
                                    "correct_value": "Đúng",
                                    "explanation": f"Áp dụng các quy tắc đạo hàm cơ bản ta có: $f'(x) = 3x^2 - {6 * exam_num}x$."
                                },
                                {
                                    "label": "b",
                                    "text": f"Hàm số đạt cực đại tại điểm $x = {2 * exam_num}$ và cực tiểu tại $x = 0$.",
                                    "correct_value": "Sai",
                                    "explanation": f"Giải phương trình $f'(x) = 0 \\Leftrightarrow x=0$ (cực đại) hoặc $x={2*exam_num}$ (cực tiểu)."
                                },
                                {
                                    "label": "c",
                                    "text": f"Đường thẳng nối hai cực trị của đồ thị có phương trình dạng $y = -{2 * (exam_num ** 2)}x + 1$.",
                                    "correct_value": "Đúng",
                                    "explanation": f"Đường thẳng qua cực trị là phần dư của phép chia $f(x)$ cho $f'(x)$, tương ứng $y = -{2*exam_num**2}x + 1$."
                                },
                                {
                                    "label": "d",
                                    "text": f"Đồ thị hàm số nhận điểm uốn $I({exam_num}; 1 - {2 * (exam_num ** 3)})$ làm tâm đối xứng.",
                                    "correct_value": "Đúng",
                                    "explanation": f"Đạo hàm cấp hai $f''(x) = 6x - {6*exam_num} = 0 \\Rightarrow x={exam_num}$."
                                }
                            ]
                        },
                        {
                            "question_number": 2,
                            "context_text": "Trong không gian tọa độ $Oxyz$, cho điểm $A(1; 2; -1)$ và đường thẳng $d: \\frac{{x-2}}{{1}} = \\frac{{y+1}}{{2}} = \\frac{{z}}{{-2}}$. Gọi $(P)$ là mặt phẳng đi qua $A$ và vuông góc với đường thẳng $d$.",
                            "statements": [
                                {
                                    "label": "a",
                                    "text": "Vectơ chỉ phương của đường thẳng $d$ là $\\vec{{u}}_d = (1; 2; -2)$.",
                                    "correct_value": "Đúng",
                                    "explanation": "Từ phương trình chính tắc của đường thẳng $d$, các hệ số dưới mẫu số là tọa độ của vectơ chỉ phương $\\vec{{u}}_d = (1; 2; -2)$."
                                },
                                {
                                    "label": "b",
                                    "text": "Mặt phẳng $(P)$ nhận vectơ chỉ phương $\\vec{{u}}_d$ làm vectơ pháp tuyến.",
                                    "correct_value": "Đúng",
                                    "explanation": "Vì $(P) \\perp d$ nên vectơ pháp tuyến $\\vec{{n}}_P = \\vec{{u}}_d = (1; 2; -2)$."
                                },
                                {
                                    "label": "c",
                                    "text": f"Phương trình tổng quát của mặt phẳng $(P)$ là $x + 2y - 2z + {exam_num} = 0$.",
                                    "correct_value": "Sai",
                                    "explanation": "Phương trình $(P): 1(x-1) + 2(y-2) - 2(z+1) = 0 \\Leftrightarrow x + 2y - 2z - 7 = 0$."
                                },
                                {
                                    "label": "d",
                                    "text": "Đường thẳng $d$ song song với mặt phẳng $(P)$.",
                                    "correct_value": "Sai",
                                    "explanation": "Vì đường thẳng $d \\perp (P)$ nên phát biểu $d \\parallel (P)$ là Sai."
                                }
                            ]
                        },
                        {
                            "question_number": 3,
                            "context_text": f"Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $a$. Cạnh bên $SA$ vuông góc với đáy và $SA = a\\sqrt{{2}}$. Gọi $\\alpha$ là góc giữa $SC$ và mặt phẳng $(SAB)$.",
                            "statements": [
                                {
                                    "label": "a",
                                    "text": "Đường thẳng $BC$ vuông góc với mặt phẳng $(SAB)$.",
                                    "correct_value": "Đúng",
                                    "explanation": "Ta có $BC \\perp AB$ và $BC \\perp SA \\Rightarrow BC \\perp (SAB)$."
                                },
                                {
                                    "label": "b",
                                    "text": "Hình chiếu vuông góc của đường thẳng $SC$ lên mặt phẳng $(SAB)$ là đường thẳng $SB$.",
                                    "correct_value": "Đúng",
                                    "explanation": "Hình chiếu của $S$ trên $(SAB)$ chính là $S$. Hình chiếu của $C$ trên $(SAB)$ là $B$ (vì $CB \\perp (SAB)$)."
                                },
                                {
                                    "label": "c",
                                    "text": "Góc giữa đường thẳng $SC$ và mặt phẳng $(SAB)$ là góc $\\widehat{{BSC}}$.",
                                    "correct_value": "Đúng",
                                    "explanation": "Góc giữa đường thẳng và mặt phẳng là góc giữa đường thẳng đó và hình chiếu của nó lên mặt phẳng. Vậy $\\alpha = \\widehat{BSC}$."
                                },
                                {
                                    "label": "d",
                                    "text": "Tam giác $SBC$ là tam giác đều.",
                                    "correct_value": "Sai",
                                    "explanation": "Tam giác $SBC$ vuông tại $B$ nên không thể là tam giác đều."
                                }
                            ]
                        },
                        {
                            "question_number": 4,
                            "context_text": "Cho hộp thứ nhất chứa 3 viên bi đỏ và 2 viên bi xanh; hộp thứ hai chứa 4 viên bi đỏ và 3 viên bi xanh. Lấy ngẫu nhiên từ mỗi hộp ra 1 viên bi.",
                            "statements": [
                                {
                                    "label": "a",
                                    "text": "Xác suất để lấy được hai viên bi cùng màu đỏ là $\\frac{{12}}{{35}}$.",
                                    "correct_value": "Đúng",
                                    "explanation": "Xác suất lấy bi đỏ từ hộp 1 là $P(R_1) = \\frac{3}{5}$. Xác suất lấy bi đỏ từ hộp 2 là $P(R_2) = \\frac{4}{7}$. Xác suất cả hai cùng đỏ là $P = \\frac{3}{5} \\times \\frac{4}{7} = \\frac{12}{35}$."
                                },
                                {
                                    "label": "b",
                                    "text": "Xác suất để lấy được hai viên bi cùng màu xanh là $\\frac{{6}}{{35}}$.",
                                    "correct_value": "Đúng",
                                    "explanation": "Xác suất lấy bi xanh từ hộp 1 là $P(G_1) = \\frac{2}{5}$. Xác suất lấy bi xanh từ hộp 2 là $P(G_2) = \\frac{3}{7}$. Xác suất cả hai cùng xanh là $P = \\frac{2}{5} \\times \\frac{3}{7} = \\frac{6}{35}$."
                                },
                                {
                                    "label": "c",
                                    "text": "Xác suất để lấy được hai viên bi khác màu là $\\frac{{17}}{{35}}$.",
                                    "correct_value": "Đúng",
                                    "explanation": "Xác suất lấy được 2 viên cùng màu là $P_{cm} = P_{đỏ} + P_{xanh} = \\frac{12}{35} + \\frac{6}{35} = \\frac{18}{35}$. Xác suất hai viên khác màu là $P = 1 - \\frac{18}{35} = \\frac{17}{35}$."
                                },
                                {
                                    "label": "d",
                                    "text": "Xác suất để có ít nhất một viên bi đỏ là $1.0$.",
                                    "correct_value": "Sai",
                                    "explanation": "Ít nhất một đỏ: $1 - P(\\text{cả hai cùng xanh}) = 1 - \\frac{6}{35} = \\frac{29}{35} \\neq 1.0$."
                                }
                            ]
                        }
                    ]
                },
                {
                    "section_id": 3,
                    "section_title": "PHẦN III. TRẢ LỜI NGẮN",
                    "questions": [
                        {
                            "question_number": 1,
                            "question_text": f"Một xưởng muốn sản xuất chiếc lon hình trụ có thể tích $V = {2 * (ans_q21 ** 3)}\\pi$ cm$^3$. Tìm bán kính đáy $R$ (cm) của lon để diện tích kim loại toàn phần làm chiếc lon đạt giá trị nhỏ nhất.",
                            "correct_answer": str(ans_q21),
                            "explanation": f"Thể tích $V = \\pi R^2 h = 2 \\cdot {ans_q21 ** 3} \\pi \\Rightarrow h = \\frac{{2 \\cdot {ans_q21 ** 3}}}{{R^2}}$. Diện tích toàn phần $S(R) = 2\\pi R h + 2\\pi R^2 = \\frac{{4\\pi \\cdot {ans_q21 ** 3}}}{{R}} + 2\\pi R^2$. Đạo hàm $S'(R) = -\\frac{{4\\pi \\cdot {ans_q21 ** 3}}}{{R^2}} + 4\\pi R = 0 \\Leftrightarrow R = {ans_q21}$ cm."
                        },
                        {
                            "question_number": 2,
                            "question_text": f"Tìm số hạng đầu $u_1$ của cấp số cộng $(u_n)$ biết tổng của 15 số hạng đầu tiên của nó bằng ${(ans_q22 + 21) * 15}$ và công sai $d = 3$.",
                            "correct_answer": str(ans_q22),
                            "explanation": f"Ta có $S_{{15}} = \\frac{{15}}{{2}}[2u_1 + 14(3)] = {(ans_q22 + 21) * 15} \\Leftrightarrow \\frac{{1}}{{2}}[2u_1 + 42] = {ans_q22 + 21} \\Leftrightarrow u_1 + 21 = {ans_q22 + 21} \\Leftrightarrow u_1 = {ans_q22}$."
                        },
                        {
                            "question_number": 3,
                            "question_text": f"Có bao nhiêu số tự nhiên chẵn gồm 4 chữ số đôi một khác nhau được lập từ tập hợp gồm {exam_num + 5} chữ số từ 1 đến {exam_num + 5}?",
                            "correct_answer": "360" if exam_num < 2 else str(ans_q23),
                            "explanation": "Số cách lập số tự nhiên chẵn được tính bằng việc chọn chữ số hàng đơn vị chẵn trước, sau đó chọn 3 chữ số khác nhau xếp vào 3 vị trí còn lại."
                        },
                        {
                            "question_number": 4,
                            "question_text": f"Tính diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = x^2$ và đường thẳng $y = -x + {2 * exam_num}$ (Lấy kết quả làm tròn đến 2 chữ số thập phân).",
                            "correct_answer": "4.5" if exam_num == 1 else "12.33",
                            "explanation": "Phương trình hoành độ giao điểm, sau đó tích phân hiệu hai đồ thị trên khoảng hai nghiệm."
                        },
                        {
                            "question_number": 5,
                            "question_text": f"Trong không gian $Oxyz$, tìm khoảng cách ngắn nhất từ gốc tọa độ $O(0;0;0)$ đến đường thẳng $d: \\{{x = 2 + t, y = 2 - t, z = {exam_num}\\}}.",
                            "correct_answer": str(exam_num + 2),
                            "explanation": "Tính khoảng cách từ điểm đến đường thẳng bằng công thức tích có hướng hoặc lập hàm số cực tiểu."
                        },
                        {
                            "question_number": 6,
                            "question_text": f"Một người gửi 100 triệu đồng vào ngân hàng với lãi suất {exam_num + 5}%/năm lãi kép. Hỏi sau tối thiểu bao nhiêu năm người đó nhận được số tiền gấp đôi ban đầu?",
                            "correct_answer": "10" if exam_num == 3 else "12",
                            "explanation": "Sử dụng bất phương trình lãi kép $100(1 + r)^n > 200$, tìm n tối thiểu."
                        }
                    ]
                }
            ]
        }
        exams.append(exam)
    return exams

def seed_db():
    print("Recreating database tables...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        json_path = os.path.join(os.path.dirname(__file__), "exams_data.json")
        
        # Auto-generate file if missing
        if not os.path.exists(json_path):
            print("exams_data.json not found. Auto-generating default 6 exams...")
            default_exams = get_default_exams_json()
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(default_exams, f, ensure_ascii=False, indent=2)
        
        print(f"Reading and seeding exams from {json_path}...")
        with open(json_path, "r", encoding="utf-8") as f:
            exams = json.load(f)

        for exam in exams:
            exam_title = exam.get("exam_title", "Đề thi thử")
            sections = exam.get("sections", [])
            try:
                print(f"Seeding {exam_title}...")
            except UnicodeEncodeError:
                print(f"Seeding: {exam_title.encode('ascii', 'ignore').decode('ascii')}...")
            
            for section in sections:
                section_title = section.get("section_title", "")
                section_id = section.get("section_id")
                
                # PHẦN I: Trắc nghiệm khách quan
                if "PHẦN I" in section_title.upper() or section_id == 1:
                    for q in section.get("questions", []):
                        choices = q.get("choices", {})
                        options = [
                            f"A. {choices.get('A', '')}",
                            f"B. {choices.get('B', '')}",
                            f"C. {choices.get('C', '')}",
                            f"D. {choices.get('D', '')}"
                        ]
                        db.add(Question(
                            subject="math",
                            exam_name=exam_title,
                            topic="Trắc nghiệm khách quan",
                            difficulty="medium",
                            content=q.get("question_text", ""),
                            options=options,
                            correct_answer=q.get("correct_answer", ""),
                            explanation=q.get("explanation", "")
                        ))

                # PHẦN II: Trắc nghiệm Đúng/Sai
                elif "PHẦN II" in section_title.upper() or section_id == 2:
                    for q in section.get("questions", []):
                        context = q.get("context_text", "")
                        for st in q.get("statements", []):
                            label = st.get("label", "a")
                            correct_val = "A" if st.get("correct_value", "") == "Đúng" else "B"
                            content_text = f"**Câu hỏi lớn (Trắc nghiệm Đúng/Sai)**: {context}\n\n**Phát biểu {label})**: {st.get('text', '')}"
                            db.add(Question(
                                subject="math",
                                exam_name=exam_title,
                                topic="Trắc nghiệm Đúng/Sai",
                                difficulty="medium",
                                content=content_text,
                                options=["Đúng", "Sai"],
                                correct_answer=correct_val,
                                explanation=st.get("explanation", "")
                            ))

                # PHẦN III: Điền đáp án ngắn
                elif "PHẦN III" in section_title.upper() or section_id == 3:
                    for q in section.get("questions", []):
                        db.add(Question(
                            subject="math",
                            exam_name=exam_title,
                            topic="Trả lời ngắn",
                            difficulty="medium",
                            content=q.get("question_text", ""),
                            options=[],
                            correct_answer=q.get("correct_answer", ""),
                            explanation=q.get("explanation", "")
                        ))

        db.commit()
        print("Database seeded successfully from JSON!")

    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}")
        raise e
    finally:
        db.close()

if __name__ == "__main__":
    seed_db()
