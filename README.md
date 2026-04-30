# 💰 Money Tracker App (Fullstack)

Красивое и функциональное приложение для учета финансов. Позволяет регистрироваться, управлять транзакциями (доходы/расходы) и видеть актуальный баланс в реальном времени.

## 🚀 Стек технологий

*   **Backend:** Django REST Framework (DRF) + Token Authentication
*   **Frontend:** React (Vite) + TypeScript / Tailwind CSS
*   **DevOps:** Docker, Docker Compose

---

## 🛠 Запуск проекта (Docker)

Проект полностью контейнеризирован. Для запуска вам нужен только Docker и Docker Compose.

1.  **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com
    cd transaction_app
    ```

2.  **Запустите контейнеры:**
    ```bash
    docker-compose up --build
    ```

3.  **Примените миграции (в новом терминале):**
    ```bash
    docker-compose exec backend python manage.py migrate
    ```

4.  **Проект доступен по адресам:**
    *   Фронтенд: [http://localhost:5173](http://localhost:5173)
    *   Бэкенд (API): [http://localhost:8000/api](http://localhost:8000/api)

---

## 📋 API Контракт

### Авторизация
*   `POST /api/auth/register` — Регистрация (Email, Password, Name)
*   `POST /api/auth/login` — Вход (получение токена)
*   `GET /api/auth/me` — Получение данных текущего пользователя

### Транзакции
*   `GET /api/transactions` — Список всех операций + Summary (баланс, доходы, расходы)
*   `POST /api/transactions` — Создание новой записи
*   `PATCH /api/transactions/:id` — Частичное обновление
*   `DELETE /api/transactions/:id` — Удаление записи

---

## 🏗 Структура проекта

*   `/back` — Django проект (API логика, модели данных, кастомный User с UUID).
*   `/vibe_frontend_rev2-master` — React приложение на Vite (интерфейс, хранилище авторизации).
*   `docker-compose.yml` — конфигурация для одновременного запуска обоих сервисов.

---

## 👨‍💻 Автор
**Vladgrad**
