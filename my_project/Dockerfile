FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput
RUN chmod +x wait-for-db.sh

CMD ["./wait-for-db.sh", "python", "manage.py", "runserver", "0.0.0.0:8000"]
