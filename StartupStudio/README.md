# Биржа проектов. 
Это платформа, где студенты могут: 
- выкладывать свои проекты 
- создавать различные ивенты
- учавствовать в чужих ивентах.

Данный проект был форкнут и будет дорабатываться

Стек:
- django
- postgresql

Для работы нужно:

- Установить драйвер psycopg2 для postrgesql
```
pip install psycopg2-binary
```
- Установить markdownx
```
pip install django-markdownx
```
- Установить crispy-forms 
```
pip install crispy-bootstrap4
```
Активация виртуальной среды
- source env/bin/activate
Миграции
- python3 manage.py makemigrations
- python3 manage.py migrate
Запуск на сервере 
- python3 manage.py runserver
