FROM python:3.11.4-slim-buster

COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt

COPY src/ /app
WORKDIR /app

CMD ["python", "main.py"]
