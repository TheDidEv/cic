# How it was created

- create virtual environment:

```bash
$ python -m venv env
```

- activate virtual environment:

```bash
# on windows
$ env\Scripts\activate

# on mac/linux
$ source env/bin/activate
```

- then we need to install packages

```bash
$ pip install django

$ pip install djangorestframework

$ pip install django-cors-headers

# for using PostgreSql, we need install psycopg2(PostgreSQL adapter for Python)
$ pip install psycopg2
```

- we can create django project

```bash
$ django-admin startproject [projectname]
```

- my next steap it`s create project and app

```bash
# create project (my name: cicback)
$ django-admin startproject [projectname]

# go to the directory with same with project name and create app (my name: cic_api)
$ python manage.py startapp [appname]
```

- make migration for change on database
```bash
# create migration
$ python manage.py makemigrations

# apply migration
$ python manage.py migrate
```

# How to start project on local machine

```bash
# go to directori with back-end
$ cd ./cicback
# run server
$ python manage.py runserver
```
