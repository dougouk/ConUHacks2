# ConUHacks2

## envrironment setup

```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## running web app locally

```shell
gunicorn ConUHacks.web:app --timeout 120
open http://localhost:8000/
```
