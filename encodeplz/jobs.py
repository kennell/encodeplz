from celery import Celery
from flask import json
import encodeplz.config

celery = Celery()
celery.config_from_object(encodeplz.config)

@celery.task
def do_something(data):
    data['done'] = True
    return json.dumps(data)