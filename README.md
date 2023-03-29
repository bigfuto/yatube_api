## Yatube_api

Проект реализует API для социальной сети Yatube.

Дает возможность просматривать записи, комментарии и сообщества.

Авторизованные пользователи могут добавлять, редактировать и удалять 

записи и комментарии, а так-же подписываться на других авторов.

Позволяет различным frontend'ам и другим приложениям взамодействовать

с проектом Yatube.

---

### Технологии:

```
Python 3.7
Django 2.2
Django REST Framework 3.12
Djoser 2.1
Simple-JWT 4.7
Drf-yasg 1.21
```

---

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/bigfuto/yatube_api.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
(python -m venv env)
```

```
source env/bin/activate
(source env/Scripts/activate)
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
(python -m pip install --upgrade pip)
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
(python manage.py migrate)
```

Запустить проект:

```
python3 manage.py runserver
(python manage.py runserver)
```

Статическая документация:

```
http://127.0.0.1:8000/redoc/
```

Динамическая документация:

```
http://127.0.0.1:8000/swagger/
```

---
### Примеры:

Для получения записей нужно отправить `GET` запрос на эндпоинт:

```
http://127.0.0.1:8000/api/v1/posts
```

Для авторизации требуется получить `JWT` токен, для этого
отправляется `POST` запрос, в теле которого переданы поля 
`username` и `password`, на эндпоинт:

```
http://127.0.0.1:8000/api/v1/jwt/create/
```

Этот токен надо будет передавать в заголовке каждого запроса, в поле `Authorization`. Перед самим токеном должно стоять ключевое слово `Bearer` и пробел.


---

### Автор:

[Иванов Илья](https://github.com/bigfuto) в рамках курса Яндекс.Практикума