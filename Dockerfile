# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY req.txt /app/req.txt

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r req.txt

# Копируем весь проект в контейнер
COPY . /app

# Запуск бота
CMD ["python", "Main.py"]