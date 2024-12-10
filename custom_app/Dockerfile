# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /custom_app

# Copy application code
COPY . .

# Install Flask
RUN pip install flask

# Expose the port the app runs on
EXPOSE 5000

# Run the Flask application
CMD ["python", "custom_app.py"]
