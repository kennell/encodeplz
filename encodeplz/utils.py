from functools import wraps
from flask import abort, request


def validate_json(f):
    """
        Checks if a requests content-type is "application/json"
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.is_json:
            return f(*args, **kwargs)
        else:
            return abort(400)
    return decorated_function
