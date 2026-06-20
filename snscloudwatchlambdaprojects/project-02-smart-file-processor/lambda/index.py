import boto3
import json
from datetime import datetime

s3 = boto3.client('s3')

ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png'}

def lambda_handler(event, context):
    results = []

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        source_key = record['s3']['object']['key']
        filename = source_key.split('/')[-1]

        # Get extension (lowercase for comparison)
        ext = ''
        if '.' in filename:
            ext = '.' + filename.rsplit('.', 1)[1].lower()

        # Decision: skip or process
        if ext not in ALLOWED_EXTENSIONS:
            log_entry = {
                "action": "SKIPPED",
                "file": source_key,
                "reason": f"Extension '{ext}' not in allowed list {list(ALLOWED_EXTENSIONS)}",
                "timestamp": datetime.utcnow().isoformat()
            }
            print(json.dumps(log_entry))
            results.append(log_entry)
            continue

        # Process: rename with timestamp and move
        try:
            name = filename.rsplit('.', 1)[0]
            timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
            new_filename = f"{name}_{timestamp}{ext}"
            destination_key = f"processed/{new_filename}"

            s3.copy_object(
                Bucket=bucket,
                CopySource={'Bucket': bucket, 'Key': source_key},
                Key=destination_key
            )
            s3.delete_object(Bucket=bucket, Key=source_key)

            log_entry = {
                "action": "PROCESSED",
                "source": source_key,
                "destination": destination_key,
                "timestamp": datetime.utcnow().isoformat()
            }
            print(json.dumps(log_entry))
            results.append(log_entry)

        except Exception as e:
            log_entry = {
                "action": "ERROR",
                "file": source_key,
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat()
            }
            print(json.dumps(log_entry))
            results.append(log_entry)

    return {'statusCode': 200, 'body': json.dumps(results)}