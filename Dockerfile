# Use the Astro runtime as base
FROM quay.io/astronomer/astro-runtime:8.3.2

# Optional: copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
