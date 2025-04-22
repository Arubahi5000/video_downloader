# Use official lightweight Python image
FROM python:3.10-slim

# Install dependencies
RUN apt update && \
    apt install -y ffmpeg curl && \
    apt clean

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Run script
CMD ["python", "download_videos.py"]