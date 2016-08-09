import redis
from uuid import uuid4
from encodeplz.app import app
from encodeplz.jobs import transcode
from encodeplz.utils import validate_json
from flask import json, jsonify, request, send_file

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


@app.route('/jobs/<job_id>', methods=['GET'])
def job_show(job_id):
    return jsonify(
        {
            'download_url': 'http://localhost:' + str(app.config['ENCODEPLZ_PORT']) + '/jobs/' + str(job_id) + "/download"
        }
    )


@app.route('/jobs/<job_id>/download', methods=['GET'])
def job_download(job_id):
    return send_file(
        r.get(job_id).decode(encoding='UTF-8')
    )