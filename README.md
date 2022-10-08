# Тестовое задание на вакансию BackEnd Dev

----------

### Стэк технологий:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

----------

### Установка:

Установите docker и docker-compose согласно официальной инструкции (
взависимости от операционной системы сервера):

- https://docs.docker.com/engine/install/
- https://docs.docker.com/compose/install/

```bash
# - Cкачайте:
git clone git@github.com:cookievii/TaskTest_HSE.git

# - Перейдите в папку infra репозитория с помощью команды ;
cd infra/

# - Запустите приложения в контейнерах:
docker-compose up -d --build

# - Создайте суперпользователя Django (Обязательные поля: username, password):
docker-compose exec backend python manage.py createsuperuser
```

 * После запуска Docker сервер доступен по ссылке:

   * Админ панель: ```GET``` ```http://127.0.0.1/admin/```
   * Доступные энтпоинты: ```GET``` ```http://127.0.0.1/api/```

----------

### Сделано:

1) Сервис умеет удалять отдельную или все trades сразу при помощи API запроса.

   !!! Разночтение по ТЗ - Сделал и то и другое.

* Пример запроса для удаления:
    * Удалить все trades:
        * Пример
          запроса: ```DELETE``` ```http://127.0.0.1/api/trades/delete_all/```

    * Удалить trades по id:
        * Пример
          запроса: ```DELETE``` ```http://127.0.0.1/api/trades/21e9ca93-f35f-46a8-bd19-1844d1695670/```

----------

2) Сервис умеет добавлять запись в trades при помощи API запроса.

    * "trades" добавляется только если пользователь с "user.id" и "user.name"
      найден в БД.
    * При добавлении "trades", каждый уникальный "symbol" записывается.


* Добавить trades:
    * Пример запроса: ```POST``` ```http://127.0.0.1/api/trades/```

````
{
    "type": "sell",
    "user": {
        "id": 1,
        "name": "admin"
    },
    "symbol": "TEST",
    "price": "2000.55",
    "timestamp": "2022-01-01 12:06:13-05:00"
}
````

----------

3) Сервис умеет получить список всех добавленных trades.

* Получить все trades:
    * Пример запроса: ```GET``` ```http://127.0.0.1/api/trades/```

* Получить trades по uuid:
    * Пример
      запроса: ```GET``` ```http://127.0.0.1/api/trades/21e9ca93-f35f-46a8-bd19-1844d1695670```

----------

4) Сервис умеет получать список добавленных trades
   сделанных под определенным пользователем.

* Получить все trades определенного пользователя по uuid:
    * Пример
      запроса: ```GET``` ```http://127.0.0.1/api/trades/?user=a882bddf-882b-432a-8e72-0846c4b9c25c```

----------

5) Сервис умеет показывать самой высокой и самой низкой цены
   (параметр price) по c определенным параметром symbol в заданный период
   времени


* Пример
  запроса: ```GET``` ```http://127.0.0.1/api/stocks/TEST/price?start=2020-06-14&end=2020-06-14```


* Обработаны ошибки:
    * Если записей с данным stockSymbol не существует.
    * Если записи есть в базе, но в заданном периоде не было сделок.

----------

### Авторы:

* **Валитов Ильмир Илсурович**
  GitHub - [cookievii](https://github.com/cookievii)

### MIT License:

Copyright (c) 2022 [cookievii](https://github.com/cookievii)

----------
