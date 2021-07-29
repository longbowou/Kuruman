# Kuruman

Django App for [Datatables](https://datatables.net) View
and [KTDatatable](https://keenthemes.com/metronic/?page=docs&section=html/components/datatable) View

## Requirements

- [Docker](https://docs.docker.com/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## How to run it?

- Clone the repository
- Build the application

```
docker-compose build
```

- Make migrations

```
docker-compose run --rm umlazi python manage.py makemigrations
```

- Run migrations

```
docker-compose run --rm umlazi python manage.py migrate
```

- Run seed database

```
docker-compose run --rm umlazi python manage.py seed
```

- Run the application

```
docker-compose up
```

## Where is the application running?

- Web App - [http://0.0.0.0:8000](http://0.0.0.0:8000/)
- PgAdmin4 - [http://0.0.0.0:5050](http://0.0.0.0:5050)
    - postgres@postgres.com
    - postgres