# Chat_Django-WebSocket

# `/chat/login/`
## ● - на входной страничке юзер задает свой юзернейм
![image](https://user-images.githubusercontent.com/55922843/160144544-727f7351-8570-4d6b-95d2-7c928952bdaa.png)
## если такового нет в базе данных - предложить юзеру задать пароль и сохранить его в базе, 
![image](https://user-images.githubusercontent.com/55922843/160144979-3f0001ad-806c-4c34-bcce-d496d1ba03eb.png)
## если есть - запросить пароль.
![image](https://user-images.githubusercontent.com/55922843/160144805-1c057c60-f79e-4c02-97ae-635015ba1143.png)
## (можно без функционала восстановления пароля). Пароль пользователя хранить в виде хеша.
![image](https://user-images.githubusercontent.com/55922843/160145166-fcf18b7f-d98e-47a7-9e03-f28c906af060.png)

# `/chat/room/:name/`
## ● При входе\выходе юзера в чат - выводить соответствующее оповещение в чат.
![image](https://user-images.githubusercontent.com/55922843/160149715-be87ba82-1b15-44fc-aaf5-ff86a4cbcbf6.png)

# `/chat/room/:name/`
## ● Каждый юзер при входе получает уникальный цвет никнейма (на текущую сессию).
![image](https://user-images.githubusercontent.com/55922843/160149921-00b6f192-245a-4eef-8411-960d6f1a0e04.png)

## ● Можно и нужно использовать фреймворки для веб-сервера (Flask, Django, ...).
# `Django`

# `/chat/room/`
## ● Дать возможность юзерам создавать свои чатрумы
![image](https://user-images.githubusercontent.com/55922843/160150763-3d1787ed-691b-4c3f-8cd8-04ae67f8dc28.png)
`/chat/room/:name/edit/`
## (другие юзеры могут подлючиться в них только после приглашения).
![image](https://user-images.githubusercontent.com/55922843/160150891-031afbc9-9dbf-406c-b178-bf021dcc6300.png)
## Информацию о юзерах в каждом чатруме хранить в базе данных (one-to-many).
![image](https://user-images.githubusercontent.com/55922843/160151347-0a10124d-1f4a-4a3a-949a-3eb4d087e36f.png)

`/chat/logging/chatroom<name>.txt`
## ● Все сообщения сохранять в лог-файл с временем сообщения и никнеймом.
![image](https://user-images.githubusercontent.com/55922843/160150645-2fcce6cc-7e0d-4a7e-9a58-ac119e487aff.png)
## Для каджого чатрума - отдельный лог-файл.
![image](https://user-images.githubusercontent.com/55922843/160150524-df1e4d67-b9e4-471b-93ba-77b80166a474.png)

## ● Использовать sqlite для хранения информации о юзерах\чатрумах.	
![image](https://user-images.githubusercontent.com/55922843/160150424-01a246f1-1d22-43c6-8b8c-58e647267862.png)

## ● Приветствуется использование ORM (peewee, django models, sqlalchemy)
![image](https://user-images.githubusercontent.com/55922843/160150318-5b0fd059-8da6-48b2-b231-ba6150bf2bc0.png)
