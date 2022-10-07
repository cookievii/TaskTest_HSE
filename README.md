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

### Сделано:
1) Сервис умеет удалять отдельную или все trades сразу при помощи API запроса. 

    !!! Разночтение по ТЗ - Сделал и то и другое.


2) Сервис умеет добавлять запись в trades при помощи API запроса. 

    !!! Разночтение по ТЗ: Юзер должен создаваться при пост запросе? или достается из БД?.

    * Реализовано:  Если "name" существует в БД - забираем ее, если "name" в БД нет - создаем новую.

* Пример JSON запроса для добавления:
````
{
    "type": "sell",
    "user": {
        "id": 11,
        "name": "Ilmir"
    },
    "symbol": "TESSS",
    "price": "2000.26",
    "timestamp": "2018-01-01 12:06:13-05:00"
}
````

3) Сервис умеет получить список всех добавленных trades


4) Сервис умеет получить список добавленных trades
сделанных под определенным пользователем (Отфильтрованный список по
user.id).


5) Сервис умеет показывать самой высокой и самой низкой цены
(параметр price) по c определенным параметром symbol в заданный период
времени

Пример запроса:
````
GET /stocks/{stockSymbol}/price?start={startDate}&end={endDate} 
````
   * Обработаны ошибки:
   
     * Если записей с данным stockSymbol не существует.
     * Если записи есть в базе, но в заданном периоде не было сделок.

#### NICE TO HAVE:
1) Вся необходимая информация и инструкции для запуска есть в README.MD.
2) REST обрабатывает ошибки и отдает консистентный ответ. 
3) Чистая реализация, производительность и поддерживаемость кода.
4) Грамотное разделение уровней.
5) Production-ready код.
----------

### Установка:

Установите docker и docker-compose согласно официальной инструкции (взависимости от операционной системы сервера):

- https://docs.docker.com/engine/install/
- https://docs.docker.com/compose/install/

```bash
# - Cкачайте:
git clone git@github.com:cookievii/TaskTest_HSE.git

# - Перейдите в папку infra репозитория с помощью команды ;
cd infra/

# - Запустите приложения в контейнерах:
docker-compose up -d --build

# - Создайте суперпользователя Django:
docker-compose exec backend python manage.py createsuperuser
```
----------

### Авторы:

* **Валитов Ильмир Илсурович**
  GitHub - [cookievii](https://github.com/cookievii)

----------

### MIT License:

Copyright (c) 2022 [cookievii](https://github.com/cookievii)

----------
