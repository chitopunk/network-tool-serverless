import json
import datetime

def getTime():
    return datetime.datetime.now().time()


def endpoint(event, context):
    current_time = getTime()
    body = {
        "message": "Hello, the current time is " + str(current_time)
    }
    
    

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
