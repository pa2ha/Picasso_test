FROM python:3.11.5

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

# Команда для запуска приложения
CMD ["python", "./Picasso/manage.py", "runserver", "0.0.0.0:8000"]
