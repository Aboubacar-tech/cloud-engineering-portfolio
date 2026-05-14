import json

def lambda_handler(event, context):
    for record in event['Records']:
        message = record['Sns']['Message']
        subject = record['Sns']['Subject']
        timestamp = record['Sns']['Timestamp']
        print(f"[CPU ALERT RECEIVED]")
        print(f"Subject: {subject}")
        print(f"Timestamp: {timestamp}")
        print(f"Message: {message}")
    return {'statusCode': 200}