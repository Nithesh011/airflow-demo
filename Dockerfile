# Use the exact Astro runtime your deployment uses
FROM quay.io/astronomer/astro-runtime:3.0-9

# Optional: install Python dependencies your DAG needs
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


