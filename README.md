# Challenge 1a: PDF Processing Solution

## Overview
This repository contains a robust solution for Challenge 1a of the Adobe India Hackathon 2025. The goal is to extract a structured outline (Title, H1, H2, H3 headings with page numbers) from PDF documents and output them as JSON files. The solution is fully containerized, modular, and meets all hackathon constraints.

## Approach
- **PDF Parsing:** Uses PyMuPDF to extract text, font size, and style from each page.
- **Heading Detection:** Applies heuristics based on font size, boldness, and text patterns (not just font size) to identify headings (H1, H2, H3).
- **Hierarchy Construction:** Assigns heading levels and page numbers, building a clean outline.
- **Fallback:** If no headings are found, generates a default outline.
- **No Hardcoding:** The logic is generic and does not rely on file-specific rules or hardcoded headings.
- **Offline & Fast:** All processing is local, with no network calls, and optimized for speed (≤10s for 50-page PDFs).

## Official Challenge Guidelines

### Submission Requirements
- **GitHub Project**: Complete code repository with working solution
- **Dockerfile**: Must be present in the root directory and functional
- **README.md**:  Documentation explaining the solution, models, and libraries used

### Build Command
```bash
docker build --platform linux/amd64 -t adobe1a:latest .
```

### Run Command
```bash
docker run -v $(pwd)/sample_dataset:/app/sample_dataset pdf-processor
```

### Critical Constraints
- **Execution Time**: ≤ 10 seconds for a 50-page PDF
- **Model Size**: ≤ 200MB (if using ML models)
- **Network**: No internet access allowed during runtime execution
- **Runtime**: Must run on CPU (amd64) with 8 CPUs and 16 GB RAM
- **Architecture**: Must work on AMD64, not ARM-specific

### Key Requirements
- **Automatic Processing**: Process all PDFs from `/app/input` directory
- **Output Format**: Generate `filename.json` for each `filename.pdf`
- **Input Directory**: Read-only access only
- **Open Source**: All libraries, models, and tools must be open source
- **Cross-Platform**: Test on both simple and complex PDFs

## Sample Solution Structure
```
Challenge_1a/
├── sample_dataset/
│   ├── outputs/         # JSON files provided as outputs.
│   ├── pdfs/            # Input PDF files
│   └── schema/          # Output schema definition
│       └── output_schema.json
├── Dockerfile           # Docker container configuration
├── process_pdfs.py      # Sample processing script
└── README.md           # This file
```

## Sample Implementation

### Current Sample Solution
The provided `process_pdfs.py` is a **basic sample** that demonstrates:
- PDF file scanning from input directory
- Dummy JSON data generation
- Output file creation in the specified format

**Note**: This is a placeholder implementation using dummy data. A real solution would need to:
- Implement actual PDF text extraction
- Parse document structure and hierarchy
- Generate meaningful JSON output based on content analysis

### Sample Processing Script (`process_pdfs.py`)
```python
# Current sample implementation
def process_pdfs():
    input_dir = Path("/app/input")
    output_dir = Path("/app/output")
    
    # Process all PDF files
    for pdf_file in input_dir.glob("*.pdf"):
        # Generate structured JSON output
        output_file = output_dir / f"{pdf_file.stem}.json"
        # Save JSON output
```

### Sample Docker Configuration
```dockerfile
FROM --platform=linux/amd64 python:3.10
WORKDIR /app
COPY process_pdfs.py .
CMD ["python", "process_pdfs.py"]
```

## Expected Output Format

### Required JSON Structure
Each PDF should generate a corresponding JSON file that **must conform to the schema** defined in `sample_dataset/schema/output_schema.json`.

## Implementation Guidelines

### Performance Considerations
- **Memory Management**: Efficient handling of large PDFs
- **Processing Speed**: Optimize for sub-10-second execution
- **Resource Usage**: Stay within 16GB RAM constraint
- **CPU Utilization**: Efficient use of 8 CPU cores

### Testing Strategy
- **Simple PDFs**: Test with basic PDF documents
- **Complex PDFs**: Test with multi-column layouts, images, tables
- **Large PDFs**: Verify 50-page processing within time limit

## Testing Your Solution

### Local Testing
```bash
# Build the Docker image
docker build --platform linux/amd64 -t pdf-processor .

# Test with sample data
docker run --rm -v $(pwd)/sample_dataset/pdfs:/app/input:ro -v $(pwd)/sample_dataset/outputs:/app/output --network none pdf-processor
```

### Validation Checklist
- [ ] All PDFs in input directory are processed
- [ ] JSON output files are generated for each PDF
- [ ] Output format matches required structure
- [ ] **Output conforms to schema** in `sample_dataset/schema/output_schema.json`
- [ ] Processing completes within 10 seconds for 50-page PDFs
- [ ] Solution works without internet access
- [ ] Memory usage stays within 16GB limit
- [ ] Compatible with AMD64 architecture

---

**Important**: This is a sample implementation. Participants should develop their own solutions that meet all the official challenge requirements and constraints.

## Libraries Used
- **PyMuPDF (fitz):** For fast, reliable PDF parsing and text extraction.
- **Python Standard Library:** For file and JSON operations.

## Compliance & Constraints
- No internet/network calls are made at any stage.
- No hardcoded file names, paths, or logic.
- Model size is well below 200MB (no ML model used).
- Runs on CPU (amd64), tested for 8 CPUs/16GB RAM.
- Output strictly matches the schema in `sample_dataset/schema/output_schema.json`.

## How to Build and Run

### Troubleshooting & FAQ
- **Q:** My output JSON is empty or missing headings?
  **A:** Check that your PDF uses extractable text (not just images). The heuristics may need tuning for unusual layouts.
- **Q:** Docker build fails on ARM?
  **A:** Use the `--platform=linux/amd64` flag as shown above.
- **Q:** Output not generated?
  **A:** Ensure `/app/output` is writable and `/app/input` contains PDFs.

## Modularity & Extensibility
- The code is modular: heading extraction and file processing are separate functions.
- You can easily extend the heuristics for multilingual or more complex heading detection.
- Designed for easy integration into future hackathon rounds.

