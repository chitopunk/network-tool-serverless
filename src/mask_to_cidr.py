import json
from src.convert import CidrMaskConvert
from src.error import error

c = CidrMaskConvert()

# e.g. http://127.0.0.1:8000/mask-to-cidr?value=255.0.0.0
def url_mask_to_cidr(event, context):
    try:
        val = event['queryStringParameters']['value']
    except:
        return error("No Val Passed")
    res = {
        "function": "MaskToCidr",
        "input": val,
        "output": c.mask_to_cidr(val),
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(res)
    }
    return response
