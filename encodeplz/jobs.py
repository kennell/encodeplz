import redis
import os.path
import tempfile
import requests
from celery import Celery
from flask import json
from encodeplz.config import CeleryConfig
from uuid import uuid4
from converter import Converter


celery = Celery()
celery.config_from_object(CeleryConfig)


r = redis.StrictRedis(host='localhost', port=6379, db=3)


@celery.task
def transcode(id, input):
    source_file = os.path.join(tempfile.gettempdir(), uuid4().hex)
    with open(source_file, mode='wb') as f:
        rsp = requests.get(input['source'], stream=True)
        for block in rsp.iter_content(1024):
            f.write(block)


    c = Converter()
    output_file =  os.path.join(tempfile.gettempdir(), uuid4().hex)
    conv = c.convert(source_file, output_file, {
        'format': 'mkv',
        'audio': {
            'codec': 'mp3',
            'samplerate': 11025,
            'channels': 2
        },
        'video': {
            'codec': 'h264',
            'width': 720,
            'height': 400,
            'fps': 5
        }})

    for percent in conv:
        pass

    r.set(id, output_file)





