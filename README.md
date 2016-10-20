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
celery -A tasks worker -l info
```

Run Flask

```bash
export FLASK_DEBUG=1
export FLASK_APP=app.py
flask run
```

## TODO

- Implement background scheduler to retry failed `requested` and `in_progress` pages
- Tests
- API docs (+ RAML stuff)
- UI?
- ???
