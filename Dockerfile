# Use official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code into the container
COPY . .

# Expose the port
EXPOSE 8080

# Run the application
CMD ["python", "src/main.py"]