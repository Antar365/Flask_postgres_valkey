# Use the official Python image as the base image
FROM python:3.9-slim

# Install PostgreSQL development dependencies
RUN apt-get update && \
    apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /project_information

# Copy the requirement.txt into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port Flask will run on
EXPOSE 8081

# Command to run the Flask app
CMD ["python", "app.py"]
