# Use the official Python image as the base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the Django app into the container
COPY ibeamroot /app/

# Expose the port that Django runs on (default is 8000)
EXPOSE 8000

# Apply migrations and collect static files
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Run the Django development server using Gunicorn
CMD ["gunicorn", "ibeamproject.wsgi:application", "--bind", "0.0.0.0:8000"]
