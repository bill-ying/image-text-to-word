# Use an official Python runtime as a parent image
FROM python:3.12.1-slim-bookworm

# Install tesseract
RUN apt update && apt install -y tesseract-ocr

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run app.py when the container launches
ENTRYPOINT ["python", "image-text-to-word.py"]
