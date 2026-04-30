FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем всё содержимое папки back в /app контейнера
COPY . .

# Устанавливаем зависимости из core/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Переходим в папку core, где лежит manage.py
WORKDIR /app/core

EXPOSE 8000
ENV PYTHONUNBUFFERED=1

# Теперь команда точно найдет manage.py
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
