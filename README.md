# Blog project
## Blog project which allows users to read and publish articles. In this Blog has been included searching function. Also user can use filters to find interesting article. For your favorite article you can put likes or make some comments. To determinate author of article in this Blog included authentication system. For creating and editing articles in this blog has been added django-ckeditor. To make Blog more SEO friendly in project added sitemap


### Инструменты разработки
 
**Стек:**

 - Python >= 3.7

- Django >= 3

- django-ckeditor==6.1.0

- Pillow==8.3.1

- sqlite3


## Установка и запуск

##### 1) Открыть терминал или консоль и перейти в нужную Вам директорию

##### 2) Клонировать репозиторий и поставить звездочку)

    https://github.com/Igor-Kuz/blog_project.git

##### 3) Создать виртуальное окружение

    python -m venv venv
    
##### 4 ) Активировать виртуальное окружение


##### 5 ) Устанавливить зависимости:

    pip install -r reqirements.txt

##### 6) Выполнить миграции

##### 7) Создать суперпользователя
    python manage.py createsuperuser


##### 8) Запустить сервер

    python manage.py runserver