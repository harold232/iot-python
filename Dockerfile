FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for opencv and easyocr
RUN apt-get update && \
    apt-get install -y build-essential libgl1 libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]