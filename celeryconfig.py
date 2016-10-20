from datetime import timedelta

BROKER_URL = 'redis://localhost'

CELERY_RESULT_BACKEND = 'redis://localhost'

CELERYBEAT_SCHEDULE = {
    'retry-unprocessed-every-minute': {
        'task': 'tasks.retry_unprocessed_pages',
        'schedule': timedelta(seconds=60),
        'relative': True,
    },
}

CELERY_TIMEZONE = 'UTC'
