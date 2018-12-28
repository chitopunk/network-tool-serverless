# Just a health check
def url_health(event, context):
    response = {
        "statusCode": 200,
        "body": "OK"
    }
    return response


