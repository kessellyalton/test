# Use the official Python image from Docker Hub
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the project files into the container
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000 to allow external access
EXPOSE 8000


# Run the application with Gunicorn as the WSGI server
CMD ["gunicorn", "innohub_website.wsgi:application", "--bind", "0.0.0.0:8000"]
