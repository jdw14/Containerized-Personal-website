FROM python:3.11-slim

WORKDIR /app

# Install pip and minimal build deps
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
# Ensure gunicorn is available for production serving
RUN pip install --no-cache-dir gunicorn

# Copy application code
COPY . /app

EXPOSE 5000

# Run with gunicorn so the container serves requests properly
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
