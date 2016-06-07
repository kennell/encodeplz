from encodeplz.app import app
from encodeplz.jobs import do_something
from encodeplz.utils import validate_json
from flask import json, jsonify, request
from uuid import uuid4


@app.route('/jobs', methods=['PUT'])
@validate_json
def job_create():
    data = json.loads(request.data)
    id = uuid4().hex
    data['id'] = id
    do_something.delay(data)
    return jsonify(
        {
            'id': id
        }
    )