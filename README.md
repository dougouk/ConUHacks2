# foody food finder

![logo](ConUHacks/image/logo_trans.png?raw=true)

## envrironment setup

```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## running web app locally

```shell
gunicorn ConUHacks.web:app
open http://localhost:8000/
```
