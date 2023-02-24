# Yatube API

## :books:Описание:
Проект является продолжением рание опубликованного проекта YaTube.
Данный проект реализован на API, что облегчит интеграцию с мобильными приложениями.

## :satellite: Технологии: 
  - Python
  - Django REST Framework
  - API REST
  - Simple-JWT

## :hammer_and_wrench: Как запустить проект:
Клонировать репозиторий на компьютер/сервер.

    git clone ....

Создать и запустить виртуальное окружение.

    Windows:
        python -m venv venv
        source venv/Scripts/activate

    Linux:
        python3 -m venv env
        source env/bin/activate
        python3 -m pip install --upgrade pip

Установить зависимости из файла requirements.txt.

    pip install -r requirements.txt

Установить миграции.

    python manage.py migrate

В файле settings.py прописать используемый домен.

    ALLOWED_HOSTS = ['список используемых доменов']

Запустить проект.

    python3 manage.py runserver


## :page_with_curl: Проектная документация:
Документация для API доступна по адресу
```
http://127.0.0.1:8000/redoc/
```

## :office_worker: Атор: 
[Ермолов Виталий](https://github.com/Flomixon)
