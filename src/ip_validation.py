import json
from src.convert import IpValidate

v = IpValidate()


# e.g. http://127.0.0.1:8000/ip-validation?value=255.0.0.0
def url_ipv4_validation(event, context):
    try:
        val = event['queryStringParameters']['value']
    except:
        val = "1"
        print("No Val Passed")
    res = {
        "function": "ipv4Validation",
        "input": val,
        "output": v.ipv4_validation(val),
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(res)
    }
    return response
