Requirements 
- Python3
- Django >=2.0, <3.0
- psycopg2-binary >=2.7, <3.0
- django-cors-headers >=2.5.2, <3.0
- graphene-django >=2.2.0, <3.0

To test local, first install

```sh
pip install -r requirements.txt
```

after run:

```sh
python3 ./manage.py runserver
```

To mount with docker with postgres

```sh
docker-compose up
```

