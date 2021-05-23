# FastAPI Boilerplate

## Project structure

```
|── app
|   |── <module_name>
|   |   |── __init__.py
|   |   |── dtos.py
|   |   |── models.py
|   |   |── router.py
|   |   |── service.py
|   |   |── test_router.py
|   |   |── test_service.py
|   |   |── config
|   |   |   |── logging.py
|   |   |   |── database.py
|   |── main.py
|   |── routes.py
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
- Environment variables: `python-dotenv`
- ORM: `sqlalchemy`
- Database migrations: `alembic`
- Unit testing: `pytest`
- ASGI server: `uvicorn`
- Process manager: `gunicorn`

---

## Code generator

```bash
fastapi gen module email
# Generated app/email
# Generated app/email/__init__.py
```

```bash
fastapi gen service email
# Generated app/email/email_service.py
# Generated app/email/test_email_service.py
```

```bash
fastapi gen resource email
# Generated app/email
# Generated app/email/__init__.py
# Generated app/email/email_service.py
# Generated app/email/test_email_service.py
# Generated app/email/email_router.py
# Generated app/email/test_email_router.py
# Generated app/email/dtos.py
# Generated app/email/models.py

```

---

## Links that might be useful

- Awesome FastAPI -- [https://awesomeopensource.com/project/mjhea0/awesome-fastapi](https://awesomeopensource.com/project/mjhea0/awesome-fastapi)
