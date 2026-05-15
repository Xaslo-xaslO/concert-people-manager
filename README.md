# Concert People Manager

**Реестр участников концертов** — внутреннее приложение для управления участниками концертных мероприятий с полной историей данных, безопасностью и удобным экспортом.

## Возможности

✅ **Управление людьми** - создание карточек с ФИО, паспортными данными, контактами  
✅ **Управление концертами** - создание событий и добавление участников галочками  
✅ **Экспорт** - Excel, PDF, CSV, DOCX с автоматической сортировкой по алфавиту  
✅ **Безопасность** - шифрование паспортных данных, RBAC, журнал действий, маскирование  
✅ **Согласие на обработку ПД** - трекинг согласия и предупреждения  
✅ **Импорт из Excel** - загрузка людей с проверкой на дубли  
✅ **Простой интерфейс** - Django Templates + HTMX для менеджеров, не программистов  

## Технический стек

- **Backend**: Python 3.12+, Django 5.0+, Django REST Framework
- **Frontend**: Django Templates + HTMX + Bootstrap 5
- **БД**: PostgreSQL
- **Контейнеризация**: Docker Compose
- **Экспорт**: openpyxl (Excel), reportlab (PDF), python-docx (DOCX)

## Требования

- Docker & Docker Compose
- Git

## Быстрый старт

### 1. Клонирование репозитория

```bash
git clone https://github.com/Xaslo-xaslo/concert-people-manager.git
cd concert-people-manager
```

### 2. Запуск через Docker Compose

```bash
docker-compose up -d
```

Проект запустится на `http://localhost:8000`

### 3. Создание администратора

```bash
docker-compose exec web python manage.py createsuperuser
```

Введите:
- Username: `admin`
- Email: `admin@concert.local`
- Password: `YourSecurePassword123!`

### 4. Загрузка тестовых данных (опционально)

```bash
docker-compose exec web python manage.py loaddata fixtures/test_data.json
```

### 5. Вход в систему

Откройте http://localhost:8000 и введите учетные данные администратора.

## Структура проекта

```
concert-people-manager/
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── requirements.txt
├── .env.example
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── apps/
│   ├── accounts/
│   ├── people/
│   ├── events/
│   ├── exports/
│   ├── audit/
│   └── dashboard/
│
├── core/
│   ├── encryption.py
│   ├── permissions.py
│   ├── validators.py
│   └── decorators.py
│
├── static/
├── templates/
├── fixtures/
└── tests/
```

## Запуск тестов

```bash
docker-compose exec web python manage.py test
```

## Что реализовано в MVP

✅ Модели и миграции  
✅ Аутентификация и RBAC  
✅ Управление людьми и концертами  
✅ Экспорт в Excel, PDF, DOCX, CSV  
✅ Импорт из Excel  
✅ Шифрование паспортных данных  
✅ Маскирование паспорта  
✅ Журнал действий  
✅ Полный интерфейс Django Templates + HTMX  
✅ Тестовые данные и unit тесты  

## Поддержка

Проверьте логи: `docker-compose logs web`