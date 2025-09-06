# Dockerfile
FROM quay.io/astronomer/ap-airflow:2.7.3-buster

# Optional: install extra Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

