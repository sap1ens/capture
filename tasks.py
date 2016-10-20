import models
import os
import pdfkit
from celery import Celery
from celery.utils.log import get_task_logger

STORAGE = 'files/'

executor = Celery('tasks')
executor.config_from_object('celeryconfig')

logging = get_task_logger(__name__)


@executor.task
def fetch_page(id, link, name):
    _process_page(id, link, name)


@executor.task
def retry_unprocessed_pages():
    unprocessed_pages = models.find_unprocessed()
    unprocessed_pages = [row.as_dict() for row in unprocessed_pages]  # FIXME

    logging.info('Retrying {} unprocessed pages'.format(len(unprocessed_pages)))

    for page in unprocessed_pages:
        _process_page(page['id'], page['link'], page['name'])


def _process_page(id, link, name):
    logging.info('Received request to fetch {}'.format(link))

    if not os.path.exists(STORAGE):
        logging.info('Creating {} folder'.format(STORAGE))
        os.makedirs(STORAGE)

    models.mark_as_in_progress(id)

    # fetch the page from URL, render PDF and save it
    pdfkit.from_url(link, STORAGE + name)

    models.mark_as_done(id)

    logging.info('Fetching finished for {}'.format(link))

if __name__ == '__main__':
    executor.start()
