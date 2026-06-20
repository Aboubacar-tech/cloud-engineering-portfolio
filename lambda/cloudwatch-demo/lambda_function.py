import json
import random

def lambda_handler(event, context):

    # Simulate real-world failures (1/3 requests fail)
    if random.randint(1, 3) == 1:
        raise Exception("Random failure - simulating production error")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Success",
            "requestId": context.aws_request_id
        })
    }