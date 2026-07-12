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
        
        # 1. MATHEMATICS QUESTIONS
        math_questions = [
            Question(
                subject="math",
                topic="Khảo sát hàm số",
                difficulty="medium",
                content="Tìm giá trị cực đại của hàm số \\(y = x^3 - 3x^2 + 2\\).",
                options=[
                    "A. \\(y_{CĐ} = 2\\)",
                    "B. \\(y_{CĐ} = 0\\)",
                    "C. \\(y_{CĐ} = -2\\)",
                    "D. \\(y_{CĐ} = 4\\)"
                ],
                correct_answer="A",
                explanation="Ta có đạo hàm \\(y' = 3x^2 - 6x = 3x(x - 2)\\). Lập bảng biến thiên ta thấy hàm số đạt cực đại tại \\(x = 0\\). Giá trị cực đại tương ứng là \\(y(0) = 2\\).",
                step_by_step=[
                    {"step": "Tính đạo hàm", "detail": "\\(y' = 3x^2 - 6x = 3x(x-2)\\)."},
                    {"step": "Tìm nghiệm đạo hàm", "detail": "\\(y' = 0 \\Leftrightarrow \\left[ \\begin{array}{l} x = 0 \\\\ x = 2 \\end{array} \\right.\\)"},
                    {"step": "Lập bảng biến thiên", "detail": "Đạo hàm đổi dấu từ dương sang âm khi đi qua điểm \\(x = 0\\), do đó \\(x = 0\\) là điểm cực đại."},
                    {"step": "Tính giá trị cực đại", "detail": "Thay \\(x = 0\\) vào hàm số ban đầu ta được: \\(y_{CĐ} = 0^3 - 3(0)^2 + 2 = 2\\)."}
                ],
                formulas=[
                    "\\left(x^n\\right)' = n \\cdot x^{n-1}",
                    "f'(x_0) = 0 \\text{ và } f''(x_0) < 0 \\Rightarrow x_0 \\text{ là điểm cực đại}"
                ]
            ),
            Question(
                subject="math",
                topic="Khảo sát hàm số",
                difficulty="easy",
                content="Cho hàm số \\(y = \\frac{2x - 1}{x + 1}\\). Tìm đường tiệm cận đứng của đồ thị hàm số.",
                options=[
                    "A. \\(x = 2\\)",
                    "B. \\(x = -1\\)",
                    "C. \\(y = 2\\)",
                    "D. \\(y = -1\\)"
                ],
                correct_answer="B",
                explanation="Đường tiệm cận đứng của hàm số dạng tiệm cận phân thức bậc nhất là nghiệm của mẫu số: \\(x + 1 = 0 \\Leftrightarrow x = -1\\).",
                step_by_step=[
                    {"step": "Xác định tập xác định", "detail": "Mẫu số xác định khi \\(x + 1 \\neq 0 \\Leftrightarrow x \\neq -1\\). TẬP XÁC ĐỊNH: \\(D = \\mathbb{R} \\setminus \\{-1\\}\\)."},
                    {"step": "Tính giới hạn", "detail": "Ta có: \\(\\lim_{x \\to -1^+} \\frac{2x - 1}{x + 1} = -\\infty\\) và \\(\\lim_{x \\to -1^-} \\frac{2x - 1}{x + 1} = +\\infty\\)."},
                    {"step": "Kết luận tiệm cận đứng", "detail": "Vì giới hạn tại vô cực tiến tới vô cùng khi \\(x \\to -1\\), đường thẳng \\(x = -1\\) là tiệm cận đứng của đồ thị hàm số."}
                ],
                formulas=[
                    "\\lim_{x \\to x_0^\\pm} f(x) = \\pm\\infty \\Rightarrow x = x_0 \\text{ là tiệm cận đứng}"
                ]
            ),
            Question(
                subject="math",
                topic="Tích phân",
                difficulty="hard",
                content="Tính tích phân \\(I = \\int_{0}^{1} x \\cdot e^x \\, dx\\).",
                options=[
                    "A. \\(I = 1\\)",
                    "B. \\(I = e\\)",
                    "C. \\(I = e - 1\\)",
                    "D. \\(I = e - 2\\)"
                ],
                correct_answer="A",
                explanation="Sử dụng phương pháp tích phân từng phần với \\(u = x\\) và \\(dv = e^x dx\\). Ta tính được nguyên hàm là \\((x-1)e^x\\), thế cận từ 0 đến 1 thu được kết quả bằng 1.",
                step_by_step=[
                    {"step": "Đặt ẩn phụ tích phân từng phần", "detail": "Đặt \\(\\begin{cases} u = x \\\\ dv = e^x dx \\end{cases} \\Rightarrow \\begin{cases} du = dx \\\\ v = e^x \\end{cases}\\)"},
                    {"step": "Áp dụng công thức tích phân từng phần", "detail": "Công thức: \\(\\int u \\, dv = u v - \\int v \\, du\\). Do đó: \\(I = \\left. x e^x \\right|_{0}^{1} - \\int_{0}^{1} e^x \\, dx\\)."},
                    {"step": "Tính toán nguyên hàm còn lại", "detail": "\\(I = (1 \\cdot e^1 - 0) - \\left. e^x \\right|_{0}^{1} = e - (e^1 - e^0) = e - e + 1 = 1\\)."}
                ],
                formulas=[
                    "\\int u \\, dv = u v - \\int v \\, du"
                ]
            ),
            Question(
                subject="math",
                topic="Tích phân",
                difficulty="medium",
                content="Diện tích hình phẳng giới hạn bởi đường cong \\(y = x^2 - 4x + 3\\) và trục hoành \\(Ox\\) là bao nhiêu?",
                options=[
                    "A. \\(\\frac{4}{3}\\)",
                    "B. \\(\\frac{2}{3}\\)",
                    "C. \\(\\frac{8}{3}\\)",
                    "D. \\(4\\)"
                ],
                correct_answer="A",
                explanation="Phương trình hoành độ giao điểm: \\(x^2 - 4x + 3 = 0 \\Leftrightarrow x = 1\\) hoặc \\(x = 3\\). Diện tích \\(S = \\int_{1}^{3} |x^2 - 4x + 3| \\, dx = - \\int_{1}^{3} (x^2 - 4x + 3) \\, dx = \\frac{4}{3}\\).",
                step_by_step=[
                    {"step": "Tìm hoành độ giao điểm", "detail": "Giải phương trình hoành độ: \\(x^2 - 4x + 3 = 0 \\Leftrightarrow (x-1)(x-3) = 0 \\Leftrightarrow x = 1 \\text{ hoặc } x = 3\\)."},
                    {"step": "Thiết lập biểu thức diện tích", "detail": "Vì \\(x^2 - 4x + 3 \\leq 0\\) trên đoạn \\([1, 3]\\), diện tích bằng: \\(S = \\int_{1}^{3} -(x^2 - 4x + 3) \\, dx\\)."},
                    {"step": "Tính tích phân xác định", "detail": "\\(S = \\left. \\left( -\\frac{x^3}{3} + 2x^2 - 3x \\right) \\right|_{1}^{3} = (-9 + 18 - 9) - \\left( -\\frac{1}{3} + 2 - 3 \\right) = 0 - \\left( -\\frac{4}{3} \\right) = \\frac{4}{3}\\)."}
                ],
                formulas=[
                    "S = \\int_{a}^{b} |f(x)| \\, dx"
                ]
            ),
            Question(
                subject="math",
                topic="Hình học không gian",
                difficulty="medium",
                content="Cho khối chóp \\(S.ABC\\) có đáy \\(ABC\\) là tam giác vuông tại \\(B\\), \\(AB = a\\), \\(BC = a\\sqrt{3}\\). Cạnh bên \\(SA\\) vuông góc với mặt phẳng đáy và \\(SA = 2a\\). Tính thể tích \\(V\\) của khối chóp \\(S.ABC\\).",
                options=[
                    "A. \\(V = \\frac{a^3\\sqrt{3}}{3}\\)",
                    "B. \\(V = a^3\\sqrt{3}\\)",
                    "C. \\(V = \\frac{2a^3\\sqrt{3}}{3}\\)",
                    "D. \\(V = \\frac{a^3\\sqrt{3}}{6}\\)"
                ],
                correct_answer="A",
                explanation="Diện tích đáy \\(S_{\\Delta ABC} = \\frac{1}{2} AB \\cdot BC = \\frac{a^2\\sqrt{3}}{2}\\). Thể tích \\(V = \\frac{1}{3} S_{đáy} \\cdot h = \\frac{1}{3} \\cdot \\frac{a^2\\sqrt{3}}{2} \\cdot 2a = \\frac{a^3\\sqrt{3}}{3}\\).",
                step_by_step=[
                    {"step": "Tính diện tích đáy tam giác vuông", "detail": "Đáy là tam giác vuông tại B: \\(S_{đáy} = \\frac{1}{2} \\cdot AB \\cdot BC = \\frac{1}{2} \\cdot a \\cdot a\\sqrt{3} = \\frac{a^2\\sqrt{3}}{2}\\)."},
                    {"step": "Tính thể tích khối chóp", "detail": "Chiều cao chóp là \\(h = SA = 2a\\). Áp dụng công thức thể tích khối chóp: \\(V = \\frac{1}{3} \\cdot S_{đáy} \\cdot h = \\frac{1}{3} \\cdot \\frac{a^2\\sqrt{3}}{2} \\cdot 2a = \\frac{a^3\\sqrt{3}}{3}\\)."}
                ],
                formulas=[
                    "V = \\frac{1}{3} \\cdot S_{base} \\cdot h",
                    "S_{\\Delta} = \\frac{1}{2} \\cdot \\text{cạnh góc vuông}_1 \\cdot \\text{cạnh góc vuông}_2"
                ]
            )
        ]
        for q in math_questions:
            db.add(q)

        # 2. LITERATURE QUESTIONS
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
            ),
            Question(
                subject="literature",
                topic="Thơ ca kháng chiến",
                difficulty="medium",
                content="Bài thơ 'Đất Nước' của Nguyễn Khoa Điềm thuộc thể loại hay chương thứ mấy trong trường ca nào?",
                options=[
                    "A. Chương V của trường ca 'Mặt đường khát vọng'",
                    "B. Chương III của trường ca 'Mặt đường khát vọng'",
                    "C. Trích trong tập thơ 'Đất ngoại ô'",
                    "D. Chương VII của trường ca 'Mặt đường khát vọng'"
                ],
                correct_answer="A",
                explanation="Đoạn trích 'Đất Nước' thuộc chương V của trường ca 'Mặt đường khát vọng' (hoàn thành năm 1971 tại chiến trường Trị Thiên).",
                step_by_step=[],
                formulas=[]
            )
        ]
        for q in lit_questions:
            db.add(q)

        # 3. ENGLISH QUESTIONS
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
            ),
            Question(
                subject="english",
                topic="Cloze Test",
                difficulty="medium",
                content="Choose the correct word to fill in blank (1): 'The library is a place where you can find books, magazines, and newspapers. In today's digital era, libraries are also (1) ________ internet access.'",
                options=[
                    "A. offering",
                    "B. offers",
                    "C. offered",
                    "D. offer"
                ],
                correct_answer="A",
                explanation="The sentence structure uses present continuous ('are also offering') to show current active services provided by libraries.",
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
                    {"section": "2. Đoạn đường đưa vợ nhặt về xóm ngụ cư", "content": "Sự ngạc nhiên của người dân xóm ngụ cư. Vẻ ngượng ngùng nhưng ẩn chứa niềm vui len lỏi trong lòng Tràng và thị."},
                    {"section": "3. Cuộc gặp gỡ giữa bà cụ Tứ và nàng dâu mới", "content": "Tâm trạng phức tạp của bà cụ Tứ: ngạc nhiên, lo lắng cho tương lai của con, thương cảm cho người đàn bà khốn khổ, cố gắng nhóm lên niềm vui gia đình."},
                    {"section": "4. Buổi sáng hôm sau và niềm tin tương lai", "content": "Bữa cơm ngày đói với nồi cháo cám đắng chát. Hình ảnh lá cờ đỏ sao vàng hiện lên trong tâm trí Tràng hứa hẹn sự đổi đời."}
                ],
                keywords=["Nạn đói 1945", "Tình cảm gia đình", "Khát vọng hạnh phúc", "Tình huống nhặt vợ", "Bà cụ Tứ", "Lá cờ đỏ sao vàng"]
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
                    {"section": "2. Kỷ niệm ấm áp tình quân dân và cảnh sông nước thơ mộng", "content": "Đêm liên hoan văn nghệ lung linh 'Doanh trại bừng lên hội đuốc hoa' và cảnh chiều sương Châu Mộc thơ mộng hư ảo."},
                    {"section": "3. Chân dung người lính Tây Tiến hào hoa, bi tráng", "content": "Vẻ ngoài kì dị 'đoàn binh không mọc tóc', quân xanh màu lá nhưng tâm hồn mơ mộng gửi về dáng kiều thơm Hà Nội. Sự hy sinh thanh thản 'Chiến trường đi chẳng tiếc đời xanh'."},
                    {"section": "4. Lời thề gắn bó cùng Tây Tiến", "content": "Khẳng định tinh thần một đi không trở lại, tâm hồn người lính luôn gửi trọn về miền Tây xa xôi."}
                ],
                keywords=["Thiên nhiên hùng vĩ", "Chân dung người lính", "Hào hoa lãng mạn", "Lớp cha trước lớp con sau", "Bi tráng", "Sông Mã"]
            )
        ]
        for m in materials:
            db.add(m)

        print("Seeding English flashcards...")
        
        # ENGLISH FLASHCARDS
        flashcards = [
            EnglishFlashcard(word="Absorbed", ipa="[əbˈzɔːbd]", meaning="Say mê, chăm chú, đắm chìm", part_of_speech="Adjective", example="She was totally absorbed in her novel.", topic="Education"),
            EnglishFlashcard(word="Curriculum", ipa="[kəˈrɪkjələm]", meaning="Chương trình giảng dạy", part_of_speech="Noun", example="The school is introducing a new science curriculum.", topic="Education"),
            EnglishFlashcard(word="Distracted", ipa="[dɪˈstræktɪd]", meaning="Bị phân tâm, mất tập trung", part_of_speech="Adjective", example="He grew more and more distracted by the noise outside.", topic="Psychology"),
            EnglishFlashcard(word="Ecosystem", ipa="[ˈiːkəʊsɪstəm]", meaning="Hệ sinh thái", part_of_speech="Noun", example="Pollution can destroy the delicate marine ecosystem.", topic="Environment"),
            EnglishFlashcard(word="Sustainable", ipa="[səˈsteɪnəbl]", meaning="Bền vững, có thể duy trì lâu dài", part_of_speech="Adjective", example="The government is promoting sustainable energy sources.", topic="Environment"),
            EnglishFlashcard(word="Biodiversity", ipa="[ˌbaɪəʊdaɪˈvɜːsəti]", meaning="Đa dạng sinh học", part_of_speech="Noun", example="Forest fires pose a threat to regional biodiversity.", topic="Environment"),
            EnglishFlashcard(word="Innovation", ipa="[ˌɪnəˈveɪʃn]", meaning="Sự đổi mới, sáng kiến", part_of_speech="Noun", example="Technological innovation is key to economic growth.", topic="Technology"),
            EnglishFlashcard(word="Artificial", ipa="[ˌɑːtɪˈfɪʃl]", meaning="Nhân tạo", part_of_speech="Adjective", example="Artificial intelligence is transforming many industries.", topic="Technology"),
            EnglishFlashcard(word="Vulnerable", ipa="[ˈvʌlnərəbl]", meaning="Dễ bị tổn thương", part_of_speech="Adjective", example="Old people are particularly vulnerable to the flu.", topic="Society"),
            EnglishFlashcard(word="Collaborate", ipa="[kəˈlæbəreɪt]", meaning="Hợp tác, cộng tác", part_of_speech="Verb", example="Researchers from both universities collaborated on the project.", topic="Working")
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
