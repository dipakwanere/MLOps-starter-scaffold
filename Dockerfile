FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY src ./src
COPY models ./models

# Default command
CMD ["python", "src/train.py"]
