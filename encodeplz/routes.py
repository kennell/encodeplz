import redis
from uuid import uuid4
from encodeplz.app import app
from encodeplz.jobs import transcode
from encodeplz.utils import validate_json
from flask import json, jsonify, request

r = redis.StrictRedis(host='localhost', port=6379, db=3)


@app.route('/jobs', methods=['PUT'])
@validate_json
def job_create():
    id = uuid4().hex
    input = json.loads(request.data)

    transcode.delay(id, input)

    return jsonify(
        {
            'id': id,
            'input': input
        }
    )


@app.route('/jobs/<job_id>')
def job_show(job_id):
    return jsonify(
        r.get(job_id)
    )