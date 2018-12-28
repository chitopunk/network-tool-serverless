import json

def error(message):
    return {
        "statusCode": 400,
        "body": message
    }
