# 🍅 Pomodoro API

REST API для управления задачами по методике Помодоро. Проект написан на FastAPI с поддержкой OAuth-авторизации, асинхронной отправкой email через Kafka и полным покрытием тестами.

## Стек технологий

- **FastAPI** — веб-фреймворк
- **PostgreSQL** + **SQLAlchemy** + **Alembic** — база данных и миграции
- **Redis** — кэширование
- **Kafka (aiokafka)** — асинхронная отправка email-уведомлений
- **Docker** + **Docker Compose** — контейнеризация
- **pytest** — unit и интеграционные тесты

## Функциональность

### Задачи (Tasks)
- Получить список всех задач
- Создать задачу (название, количество помодоров, категория)
- Обновить название задачи
- Удалить задачу по ID

### Авторизация
- Регистрация и вход по email
- OAuth через Google
- OAuth через Яндекс

### Уведомления
- После регистрации пользователь получает приветственное письмо
- Отправка происходит асинхронно через Kafka-топик

## Запуск проекта

### Требования
- Docker
- Docker Compose

### Установка

```bash
git clone https://github.com/lefyers/Pomodoro.git
cd Pomodoro
```

Создай `.local.env` файл с переменными окружения (пример в `.env.example`).

```bash
docker compose build
docker compose up -d
```

API будет доступен по адресу: `http://localhost:8000/docs`

## Тесты

```bash
# Unit тесты (без зависимостей)
poetry run pytest tests/unit

# Интеграционные тесты (нужен запущенный Docker)
poetry run pytest tests/integration
```

## Архитектура

```
app/
├── users/
│   ├── auth/client   # Авторизация (email, Google, Yandex OAuth)
├── tasks/            # CRUD задач
├── broker/           # Kafka producer
└── infrastructure/   # Настройки, база данных
tests/
├── unit/             # Unit тесты с fake-репозиториями
└── integration/      # Интеграционные тесты с реальной БД
```