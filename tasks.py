import logging

import models
import os
import pdfkit
from celery import Celery

STORAGE = 'files/'

executor = Celery('tasks', broker='redis://localhost', backend='redis://localhost')


@executor.task
def fetch_page(link, path):
    # logging.info('Received request to fetch {}'.format(page.as_json()))

    if not os.path.exists(STORAGE):
        # logging.info('Creating {} folder'.format(STORAGE))
        os.makedirs(STORAGE)

    # fetch the page from URL, render PDF and save it
    pdfkit.from_url(link, STORAGE + path)

    # mark work as done
    # models.mark_as_done(page.id)

    # logging.info('Fetching finished for {}'.format(page.as_json()))


if __name__ == '__main__':
    executor.start()
