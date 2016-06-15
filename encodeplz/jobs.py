from celery import Celery
from flask import json
from encodeplz.config import CeleryConfig
from time import sleep

celery = Celery()
celery.config_from_object(CeleryConfig)

@celery.task
def do_something(data):
    data['done'] = True
    sleep(2)
    return json.dumps(data)