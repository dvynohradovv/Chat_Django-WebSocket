# Simple chat app on Django and WebSocket
***
<img src="https://user-images.githubusercontent.com/55922843/160144544-727f7351-8570-4d6b-95d2-7c928952bdaa.png" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="650" height="500" />

# Endpoints:
***
- `/chat/login/`
- `/chat/room/:name/`
- `/chat/room/`
- `/chat/room/:name/edit/`

# Requirements
***
- **Python > 3.9**

# Run
***
- **Install virtualenv:** `pip install virtualenv`

- **Create virtual environment:** `virtualenv env` or `python -m venv env`

- **Activate virtualenv:**

    **unix:** `source env/Scripts/activate`
  
    **windows:** `env/Scripts/activate.bat`

- **Install all requirements:** `pip install -r requirements.txt`

- **Run all migrations:** `python manage.py migrate`
  
- **Run local server:** `python manage.py runserver`
