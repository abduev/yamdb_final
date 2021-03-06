# Проект YaMDb


## Описание проекта
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Благодарные или возмущённые читатели оставляют к произведениям текстовые отзывы (Review) и выставляют произведению рейтинг (оценку в диапазоне от одного до десяти). Из множества оценок высчитывается средняя оценка произведения.

## Содержание проекта
Проект выполнен на фреймворке Django, API к проекту - на Django REST Framework.
Реализована контейнеризация с помощью Docker.


## Сценарии

__Неавторизованный пользователь__ может:
 - просматривать описания произведений
 - читать отзывы и комментарии

__Авторизованный пользователь__ может:
 - сценарии неавторизованного пользователя
 - публиковать отзывы и ставить рейтинг произведениям
 - комментировать чужие отзывы и ставить им оценки
 - редактировать и удалять свои отзывы и комментарии

__Модератор__ может:
 - сценарии авторизованного пользователя
 - удалять любые отзывы и комментарии

__Администратор__ может:
 - полные права на управление проектом
 - создавать и удалять категории и произведения
 - назначать роли пользователям.

![yamdb workflow](https://github.com/abduev/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
## Установка и запуск
Требования:
 - Python 3.8+
 - Git
 - Docker

В докере используются одна БД PostgreSQL и один сервер Nginx. Для хранения данных используются тома (volumes).
Скопируйте проект с ГитХаба:
```sh
git clone https://github.com/abduev/infra_sp2.git
```

В корневой директории проекта создайте файл "__.env__" и скопируйте туда переменные окружения из файла "__dev.env__".


Запустите сборку проекта:
```sh
docker-compose up -d
```

После завершения сборки необходимо выполнить несколько шагов.

Загрузить статику.
 ```sh
docker-compose exec web python manage.py collectstatic --no-input
```
Создать суперпользователя.
 ```sh
docker-compose exec web python manage.py createsuperuser
```

Проект готов к работе. Документация к API проекта: http://127.0.0.1/redoc/.


Для остановки проекта выполните команду:
```sh
docker-compose down
```

