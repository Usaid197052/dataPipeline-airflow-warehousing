FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install pandas requests pymysql cryptography

CMD ["python", "scripts/run_pipeline.py"]