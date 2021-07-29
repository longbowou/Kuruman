# Kuruman

A sample project that uses [django-ktdatatable-view](https://pypi.org/project/django-ktdatatable-view) and
[django-datatables-view](https://pypi.org/project/django-datatables-view)

## Requirements

- [Docker](https://docs.docker.com/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## How to run it?

- Clone the repository
- Build the application

```bash
docker-compose build
```

- Make migrations

```bash
docker-compose run --rm kuruman python manage.py makemigrations
```

- Run migrations

```bash
docker-compose run --rm kuruman python manage.py migrate
```

- Run seed database

```bash
docker-compose run --rm kuruman python manage.py seed
```

- Run the application

```bash
docker-compose up
```

## Where is the application running?

- Web App - [http://0.0.0.0:8000](http://0.0.0.0:8000/)
