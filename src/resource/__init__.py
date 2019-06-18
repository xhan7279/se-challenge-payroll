RESOURCE_NOT_FOUND = 400
RESOURCE_OK = 200


def error_resp(message):
    resp = {}
    resp['Status'] = 'Error'
    resp['Message'] = message
    return resp


def success_resp(message=None):
    resp = {}
    resp['Status'] = 'Success'
    if message != None:
        resp['Message'] = message
    return resp
