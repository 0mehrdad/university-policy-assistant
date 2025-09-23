# Use official Python base image
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# Upgrade pip before installing deps
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["bash", "-c", "python src/ingest.py && streamlit run src/app.py --server.port=8501 --server.address=0.0.0.0"]
