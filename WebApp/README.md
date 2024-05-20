### Setup:
``` sh
python -m venv venv
pip install -r requirements.txt
```

### Setup database:
``` sh
python -m flask --app webapp db init
python -m flask --app webapp db migrate
python -m flask --app webapp db upgrade
```

### Run the app:
``` sh
python -m flask --app webapp run --port 8000 --debug
```