# Планирование рабочего расписания

Система для планирования рабочего расписания сотрудников с учетом их пожеланий.

## Возможности

- Просмотр текущего расписания
- Указание желаемых выходных на следующую неделю
- Просмотр статистики отработанных смен по месяцам

## Технологии

- Python 3.12
- Django 5.2
- PostgreSQL
- Bootstrap 5

## Установка

1. Клонируйте репозиторий:
```bash
git clone git@github.com:Dialol/work_shedule.git
cd work_shedule
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# или
.venv\Scripts\activate  # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Запустите PostgreSQL (через Docker):
```bash
docker-compose up -d
```

5. Примените миграции:
```bash
python manage.py migrate
```

6. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

## Запуск

```bash
python manage.py runserver
```

Приложение будет доступно по адресу: http://127.0.0.1:8000/

Админ-панель: http://127.0.0.1:8000/admin/
