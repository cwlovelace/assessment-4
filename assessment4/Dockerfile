# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables to prevent Python from writing pyc files to disc (optional)
ENV PYTHONDONTWRITEBYTECODE 1
# Set environment variables to prevent Python from buffering stdout and stderr (optional)
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install system dependencies (you can add any system dependencies you need here)
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /code
COPY . /code/

# Command to run the django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
