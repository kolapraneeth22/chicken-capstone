# Use a smaller Python base image
FROM python:3.8-slim-buster

# Install required packages
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends awscli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy only the requirements first for caching
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the remaining application files
COPY . /app

# Command to run the application
CMD ["python3", "app.py"]
