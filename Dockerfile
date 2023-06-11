FROM python:3.11.4-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py", "--start-time", "2023-06-10 00:00:00"]
