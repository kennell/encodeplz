from encodeplz.app import app
from encodeplz.jobs import do_something
from encodeplz.utils import validate_json
from flask import json, jsonify, request, Response
from uuid import uuid4
from pprint import pprint

@app.route('/jobs', methods=['PUT'])
@validate_json
def job_create():
    data = json.loads(request.data)
    job = do_something.delay(data)
    return jsonify(
        {
            'id': job.id
        }
    )


@app.route('/jobs/<job_id>')
def job_read(job_id):
    return Response(
        response=do_something.AsyncResult(job_id).get(),
        status=200,
        mimetype="application/json"
    )
