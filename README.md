# capture

Sharpening my Python skills. Using Flask, SQLAlchemy (with Postgres) and Celery (with Redis) for simple web content capturing tool (like https://getpocket.com, but generating PDFs).

## Dev

Run Postgres (default options).

Run Redis:

```bash
docker run -p 6379:6379 -d redis
```

Run celery:

```bash
celery -B -A tasks worker -l info
```

Run Flask

```bash
export FLASK_DEBUG=1
export FLASK_APP=app.py
flask run
```

## TODO

- Find a way to convert Query objects in find_* methods to list of classes
- Put `in_progress` tasks back to `requested` after timeout
- Remove name field, generate it dynamically from title
- Tests
- API docs (+ RAML stuff)
- UI?
- Dockerize!
- ???
