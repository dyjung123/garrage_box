# Environment
### This app is used with Python virtual environment.
```shell
# Anyway, running django without a docker in local
$ mkdir -p time_table/app && cd time_table/app
$ python3.9 -m venv env
$ source env/bin/activate
(env)$

(env)$ pip install django==3.2.7
(env)$ django-admin startproject time_table
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```


# Create Table App
```shell
$ docker-compose up -d --build
$ docker-compose exec web python manage.py startapp table
```

Add the new app to the `INSTALLED_APPS` list in *settings.py*:
```python
INSTALLED_APPS = [
  "django.contrib.admin",
  "django.contrib.auth",
  "django.contrib.contenttypes",
  "django.contrib.sessions",
  "django.contrib.messages",
  "django.contrib.staticfiles",
  
  "table",
]
```

docker restart
```shell
$ docker-compose down -v
$ docker-compose up -d --build
```

# Create model and migration file
### Define model in *table/models.py*
```python
from django.db import models


class User(models.Model):
  id = models.AutoField(help_text="User Primary Key", primary_key=True)
  username = models.CharField(max_length=50, blank=False, null=False,
                              unique=True)
  email = models.EmailField(blank=False, null=False)
  enabled = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
```


### create migration file and migrate
```shell
$ docker-compose build -d --build

# Create migration file
$ docker-compose exec web python manage.py makemigrations

# Reflect the migration file to DB (postgreSQL in this app)
$ docker-compose exec web python manage.py migrate
```
