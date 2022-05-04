# Template chat app on Django and WebSocket
***
<img src="https://user-images.githubusercontent.com/55922843/166743451-c175e580-68e6-4d10-8f70-638748ef727e.png" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="500" height="500" />

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
