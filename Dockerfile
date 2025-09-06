# Dockerfile
FROM quay.io/astronomer/ap-airflow:2.4.3-5

# Optional: install extra Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

