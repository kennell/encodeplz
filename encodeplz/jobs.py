from celery import Celery
from flask import json
from encodeplz.config import CeleryConfig


celery = Celery()
celery.config_from_object(CeleryConfig)


@celery.task
def do_something(data):
    data['done'] = True
    return json.dumps(data)