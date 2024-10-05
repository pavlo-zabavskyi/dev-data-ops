# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12.0

# ------------------- Stage 1: Build Stage ------------------------------
FROM python:${PYTHON_VERSION}-slim AS builder

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1
# Keeps Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Set the working directory to /server
WORKDIR /app

# Copy the contents of the server directory into the container at /app
COPY server/ .

# Install dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# ------------------- Stage 2: Final Stage ------------------------------
FROM python:${PYTHON_VERSION}-slim AS base

# Set the working directory to /app
WORKDIR /app

# Copy the built dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/

# Copy the application code from the builder stage
COPY --from=builder /app /app

# Expose port 8050 for the Flask application
EXPOSE 8050

# Define the default command to run the application
CMD ["python", "main.py"]
