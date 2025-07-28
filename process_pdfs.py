import os
import json
import fitz 
from pathlib import Path

def extract_pdf_content(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        title = doc.metadata.get('title', pdf_path.stem)
        
        outline = []
        page_num = 1
        
        for page in doc:
            blocks = page.get_text("dict")["blocks"]
            
            for block in blocks:
                if "lines" in block:
                    for line in block["lines"]:
                        for span in line["spans"]:
                            text = span["text"].strip()
                            font_size = span["size"]
                            flags = span.get("flags", 0)
                            is_bold = flags & 2**4

                            if (len(text) > 3 and len(text) < 100 and 
                                (font_size > 12 or is_bold) and 
                                not text.endswith('.') and 
                                (text.isupper() or text[0].isupper())):
                                
                                if font_size > 16:
                                    level = "H1"
                                elif font_size > 14:
                                    level = "H2"
                                else:
                                    level = "H3"
                                
                                outline.append({
                                    "level": level,
                                    "text": text,
                                    "page": page_num
                                })
            
            page_num += 1
        
        doc.close()
        
        if not outline:
            outline = [
                {
                    "level": "H1",
                    "text": "Document Content",
                    "page": 1
                }
            ]
        
        return {
            "title": title,
            "outline": outline
        }
        
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        # Fallback to basic structure
        return {
            "title": pdf_path.stem,
            "outline": [
                {
                    "level": "H1",
                    "text": "Document Content",
                    "page": 1
                }
            ]
        }

def process_pdfs():
    input_dir = Path("sample_dataset/pdfs")
    output_dir = Path("sample_dataset/outputs")
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    pdf_files = list(input_dir.glob("*.pdf"))
    
    for pdf_file in pdf_files:
        structured_data = extract_pdf_content(pdf_file)

        output_file = output_dir / f"{pdf_file.stem}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(structured_data, f, indent=2, ensure_ascii=False)
        
        print(f"Processed {pdf_file.name} -> {output_file.name}")

if __name__ == "__main__":
    print("Starting processing pdfs")
    process_pdfs() 
    print("completed processing pdfs") 