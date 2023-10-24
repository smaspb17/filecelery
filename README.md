# Filecelery

### ОПИСАНИЕ:

Filecelery - это тестовый Django REST API проект, который позволяет загружать файлы на сервер, а затем асинхронно 
обрабатывать их с использованием Celery

Бэкэнд проекта разрабатан с использованием Django REST framework, включает в себя компоненты, 
необходимые для предоставления API-сервисов, такие как маршрутизация URL, сериализаторы, модели, представления,
валидация данных. DRF обеспечивает поддержку зaпросов JSON-формата. База данных - PostgreSQL.

Что было сделано в ходе работы над проектом:

    - реализована модель File, представляющая загруженные файлы. Имеет поля: file(FileField) для загрузки файла, uploaded_at(DateTimeField) с датой и временем загрузки файла, processed(BooleanField) был ли файл обработан.
    - реализован сериализатор для модели File.
    - создан эндпоинт upload/, принимающий POST-запросы для загрузки файлов. 
    - реализована Celery задача для обработки файла. Задача запускается асинхронно и изменяет поле processed модели File на True после обработки файла.
    - реализован эндпоинт files/, возвращающий список всех файлов с их данными, включая статус обработки.


### СТЕК ТЕХНОЛОГИЙ БЭКЭНДА:
Тeрминал WSL Ubuntu (нужен для запуска Celery и Redis), Python 3.10 (WSL Ubuntu), Django Rest Framework 3.14.0, 
PostgreSQL, Celery, Redis, JSON, YAML, docker-compose

### УСТАНОВКА ПРОЕКТА в docker

Клонируй репозиторий на ПК:

``` 
git clone git@github.com:smaspb17/filecelery.git
``` 
Создай файл .env с переменными окружения находясь в директории проекта filecelery/filecelery/:
``` 
cd filecelery/filecelery
``` 
``` 
nano .env
``` 
``` 
DEBUG=True
ALLOWED_HOSTS=127.0.0.1 localhost
SECRET_KEY=     <введи секретный ключ Django>
POSTGRES_DB=filecelery
POSTGRES_USER=postgres
POSTGRES_PASSWORD=   <введи пароль>
DB_HOST=db
DB_PORT=5432
```

Запусти оркестратор docker-compose в директории filcelery/:

```
docker-compose up
``` 
В браузере перейди по адресу
``` 
http://127.0.0.1:8000/api/upload/
``` 
Создай несколько объектов модели File - загружай по одному файлу и нажимай кнопку Post

Вернись в терминал и просмотри логи. Должны быть видны завершение task в worker 
и вывод: "Файл id <file.id> обработан Celery!"

В браузере перейди по адресу
``` 
http://127.0.0.1:8000/api/files/
``` 
Должен выйти ответ в формате JSON со списком записей модели File. Значение поля processed должно быть True
``` 
[
    {
        "id": 1,
        "file": "http://127.0.0.1:8000/media/files/%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80_%D1%84%D0%BE%D1%82%D0%BE_%D1%80%D0%B5%D0%B7%D1%8E%D0%BC%D0%B5.jpg",
        "uploaded_at": "2023-10-24T13:04:11.997429Z",
        "processed": true
    },
    {
        "id": 2,
        "file": "http://127.0.0.1:8000/media/files/%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80_%D1%84%D0%BE%D1%82%D0%BE_%D1%80%D0%B5%D0%B7%D1%8E%D0%BC%D0%B5_4zxJX8K.jpg",
        "uploaded_at": "2023-10-24T13:06:05.895591Z",
        "processed": true
    }
]
``` 

### В API доступны следующие эндпоинты:

* ```/api/upload/```  Post-запрос – создание объекта file модели File. 
* ```/api/files/```  Get-запрос – получение списка объектов модели File. 
### АВТОР:

Шайбаков Марат

### ЛИЦЕНЗИЯ:

нет

### КОНТАКТЫ:

smaspb17@yandex.ru
