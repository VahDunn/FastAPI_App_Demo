Simple async service for registering and accessing applications.
Python 3.12 + FastAPI + PostgreSQL 15 + Apache Kafka. Server - uvicorn.
Pytest, Uvicorn. ORM - SQLAlchemy. 
Docker + Docker Compose. 

Эндпоинты: 
'/' - базовый эндпоинт (тестовый) - показывает, что сервер запущен и работает.
'/applications/' с методом GET - ничего не принимает, возвращает список заявок с 
    пагинацией и фильтрацией по имени пользователя.
    Пример запроса для localhost через браузер:
    
'/applicatons/' с методом POST - принимает два параметра - user_name - имя пользователя
и description - описание заявки
    Пример запроса для localhost через postman 

Инструкция по запуску: 
