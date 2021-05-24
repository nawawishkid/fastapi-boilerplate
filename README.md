# FastAPI Boilerplate

## Instructions

### Run locally on your machine

1. Copy `.env.example` to `.env` by running `cp .env.example .env`.
2. Change variables in the `.env` file to your requirements.
3. Create your modules in the `app` folder. It typically consists of router (`router.py`), data transfer objects (`dtos.py`), database models (`models.py`), and a service (`<module_name>_service.py`) to handle business logic.
4. Create database migration files by running `poetry run alembic --autogenerate -m "<msg>"`.
5. Apply the migrations by running `poetry run alembic upgrade heads`.
6. Run the app in dev mode: `poetry run task dev`

### Run locally with Docker

1. Make sure that there's a MySQL server running that you can connect to.
2. Copy `.env.example` to `.env.docker` (or whatever) then change the variables within the file.
3. Create a Docker image: `docker build -t fastapi-boilerplate .`
4. Apply the migrations if you haven't already done it: `docker run --rm --env-file .env.docker fastapi-boilerplate poetry run alembic upgrade heads`
5. Run a container using the created image:

```
docker run -d --name fastapi-boilerplate \
  -p 8080:80 \
  --env-file .env.docker \
  fastapi-boilerplate
```

6. Browse to [http://localhost:8080/docs](http://localhost:8080/docs)

---

## Project structure

```
|── app
|   |── <module_name>
|   |   |── __init__.py
|   |   |── dtos.py
|   |   |── models.py
|   |   |── router.py
|   |   |── <module_name>_service.py
|   |   |── test_router.py
|   |   |── test_service.py
|   |── config.py
|   |── dependencies.py
|   |── main.py
|── migrations
|   |── versions
|   |   |── <revision_id>_<msg>.py
|   |── env.py
|── tests # for e2e tests
|── .dockerignore
|── .env.example
|── .gitignore
|── alembic.ini
|── Dockerfile
|── poetry.lock
|── pyproject.toml
|── README.md
```

## Packages

- Package mangement: `poetry`
- Task runner (like `npm run ...` in Node.js): `taskipy`
- ORM: `sqlalchemy`
- Database migrations: `alembic`
- Unit testing: `pytest`
- ASGI server: `uvicorn`
- Process manager: `gunicorn`

---

## Built-in scripts

### dev

Running FastAPI app with `uvicorn` and watch for files changes.

```bash
poetry run task dev
```

### start

Running FastAPI app with `gunicorn` in production environment.

```bash
poetry run task start
```

### test

Running tests

```bash
poetry run task test
```

---

## Future features

### Code generator

---

## Links that might be useful

- Awesome FastAPI -- [https://awesomeopensource.com/project/mjhea0/awesome-fastapi](https://awesomeopensource.com/project/mjhea0/awesome-fastapi)
