from flask import jsonify
from functools import wraps

def standard_response(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            response = f(*args, **kwargs)
            if isinstance(response, tuple):
                data, status_code = response
            else:
                data, status_code = response, 200

            standard = {
                "statusCode": status_code,
                "message": "Success" if status_code < 400 else "Error",
                "details": [data] if isinstance(data, str) else [],
            }

            if isinstance(data, dict):
                if "error" in data:
                    standard["message"] = "Error"
                    standard["details"] = [data["error"]]
                else:
                    standard["details"] = [data]

            return jsonify(standard), status_code
        except Exception as e:
            return jsonify({
                "statusCode": 500,
                "message": "Internal Server Error",
                "details": [str(e)]
            }), 500
    return wrapper
