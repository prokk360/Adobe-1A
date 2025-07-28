FROM --platform=linux/amd64 python:3.10

WORKDIR /app

RUN pip install --no-cache-dir PyMuPDF==1.23.22

COPY process_pdfs.py .
COPY sample_dataset ./sample_dataset

CMD ["python", "process_pdfs.py"]
