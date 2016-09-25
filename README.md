# capture

Sharpening my Python skills. Using Flask, SQLAlchemy (with Postgres) and Celery (with Redis) for simple web content capturing tool (like https://getpocket.com, but generating PDFs).

## Dev

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

- Fix logging
- Fix Celery -> sqlalchemy (session), use mark_as_done
- Implement in_progress state
- Implement background scheduler to retry failed `requested` and `in_progress` pages
- Tests
- API docs
- UI?
- ???
