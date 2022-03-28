from peeringdb_server.models import EnvironmentSetting
from rest_framework.views import exception_handler
from rest_framework.exceptions import Throttled


def format_wait_time(wait_time):
    """
    Format wait time in seconds to human readable format
    """
    if wait_time < 60:
        return f"{wait_time} seconds"
    elif wait_time < 3600 and wait_time > 60:
        return f"{wait_time // 60} minutes"
    else:
        return f"{wait_time // 3600} hours"

def rest_exception_handler(exc, context):

    response = exception_handler(exc, context)
    request = context.get("request")
    view = context.get("view")

    if isinstance(exc, Throttled):
        message = getattr(request, "throttle_response_message", "Request was throttled. Expected available in {time}.")
        custom_response_data = {
            "message": f"{message}".replace("{time}", format_wait_time(exc.wait)),
        }

        response.data = custom_response_data

    return response
