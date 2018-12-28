import json
from src.convert import CidrMaskConvert

c = CidrMaskConvert()

# e.g. http://127.0.0.1:8000/cidr-to-mask?value=8
def url_cidr_to_mask(event, context):
    try:
        val = event['queryStringParameters']['value']
    except:
        val = "1"
        print("No Val Passed")
    res = {
        "function": "cidrToMask",
        "input": val,
        "output": c.cidr_to_mask(val),
    }
    response = {
        "headers": {
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Credentials" : True
        },
        "statusCode": 200,
        "body": json.dumps(res)
    }
    return response
