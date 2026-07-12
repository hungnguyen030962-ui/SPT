import os
import traceback
from pypdf import PdfReader

def extract_all():
    pdf_files = [
        "1 - Đáp án đề 01 HNUE-stamped.pdf",
        "2 - Đáp án đề 02 HNUE-stamped.pdf",
        "3 - Đáp án đề 3 HNUE-stamped.pdf",
        "4 - Đáp án HNUE-stamped.pdf",
        "5 - Đáp án đề 05 HNUE-stamped.pdf",
        "6 - Đáp án đề 06 HNUE-stamped.pdf"
    ]
    
    with open("extracted_exams.txt", "w", encoding="utf-8") as outfile:
        for idx, filename in enumerate(pdf_files, 1):
            if not os.path.exists(filename):
                outfile.write(f"--- FILE NOT FOUND: {filename} ---\n\n")
                continue
                
            outfile.write(f"=========================================\n")
            outfile.write(f"DE SO {idx}: {filename}\n")
            outfile.write(f"=========================================\n\n")
            
            try:
                reader = PdfReader(filename)
                for page_idx, page in enumerate(reader.pages, 1):
                    text = page.extract_text()
                    outfile.write(f"--- PAGE {page_idx} ---\n")
                    outfile.write(text or "[No text on page]")
                    outfile.write("\n\n")
                outfile.write(f"--- SUCCESS EXTRACTING {filename} ---\n\n")
            except Exception as e:
                outfile.write(f"ERROR EXTRACTING {filename}: {str(e)}\n")
                outfile.write(traceback.format_exc())
                outfile.write("\n\n")

if __name__ == "__main__":
    extract_all()
