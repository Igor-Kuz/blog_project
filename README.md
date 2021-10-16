# Blog project
## Blog project built on the top of Django framework. he blog allows visitors to leave comments and like. Contains functionality: 
- user registration 
- user authentication 
- article creation
- adding an images to articles
- filtration
- search
- displaying the article creation date
- displaying the tag system
- displaing categories
- counting likes and dislikes
To make Blog more SEO friendly in project has been added sitemap

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