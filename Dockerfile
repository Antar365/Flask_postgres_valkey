# Use the official Python image as the base image
FROM python:3.9-slim

# Install PostgreSQL development dependencies for psycopg2
RUN apt-get update && \
    apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /project_information

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the correct port (Flask default is 5000)
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
