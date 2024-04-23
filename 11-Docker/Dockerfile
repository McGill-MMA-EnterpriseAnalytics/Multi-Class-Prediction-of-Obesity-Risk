# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application code to the working directory
COPY model_v2.txt ./
COPY docker_api.py ./
COPY requirements.txt ./
COPY train.csv ./


# Expose port 80 for the FastAPI application
EXPOSE 80
ENV PORT=80

# Run the FastAPI application using Uvicorn when the container starts
CMD ["uvicorn", "model_v2:app", "--host", "0.0.0.0", "--port", "80"]
