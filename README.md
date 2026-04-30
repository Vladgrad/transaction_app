# ⚙️ Money Tracker Backend (API)

Бэкенд-часть приложения для учета финансов, построенная на **Django REST Framework**.

## 🛠 Технологии
- **Python 3.12**
- **Django 5.1+**
- **Django REST Framework**
- **Token Authentication** (стандартные токены DRF)
- **CORS Headers** (для связи с фронтендом)

## 🚀 Быстрый запуск (через Docker)

Находясь в корне проекта, выполните:
```bash
docker-compose up --build backend
```

Примените миграции:
```bash
docker-compose exec backend python manage.py migrate
```

## 🔐 Документация API

Базовый URL: `http://localhost:8000/api`

### Авторизация

| Метод | Эндпоинт | Описание |
| :--- | :--- | :--- |
| `POST` | `/auth/register` | Регистрация (возвращает `accessToken`) |
| `POST` | `/auth/login` | Вход (возвращает `accessToken`) |
| `GET` | `/auth/me` | Данные текущего пользователя (требует токен) |

### Транзакции (требуют заголовок `Authorization: Bearer <token>`)

| Метод | Эндпоинт | Описание |
| :--- | :--- | :--- |
| `GET` | `/transactions` | Список транзакций + Summary (баланс) |
| `POST` | `/transactions` | Создание новой транзакции |
| `PATCH` | `/transactions/<id>` | Обновление (UUID) |
| `DELETE` | `/transactions/<id>` | Удаление |

## 📂 Структура приложения
- `core/` — настройки проекта (settings.py, urls.py).
- `api/` — основная логика (модели User и Transaction, вьюхи, сериализаторы).
- `requirements.txt` — список зависимостей.

## 🧪 Тестирование
Для проверки API рекомендуется использовать **Postman**. 
Не забывайте добавлять заголовок `Content-Type: application/json` для всех POST/PATCH запросов.
