FROM python:3.11

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY . /app
WORKDIR /app

EXPOSE 8000

# runs the production server
CMD ["python", "manage.py", "runserver", "localhost:8000"]