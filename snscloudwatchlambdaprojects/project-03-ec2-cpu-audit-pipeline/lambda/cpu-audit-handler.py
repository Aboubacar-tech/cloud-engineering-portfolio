import boto3
import json
from datetime import datetime

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

AUDIT_BUCKET = 'ec2-audit-logs-1'  # replace with your bucket name

def lambda_handler(event, context):
    timestamp = datetime.utcnow().isoformat()

    # Parse the SNS message
    for record in event['Records']:
        sns_message = json.loads(record['Sns']['Message'])
        alarm_name = sns_message.get('AlarmName', 'unknown')
        new_state = sns_message.get('NewStateValue', 'unknown')
        instance_id = extract_instance_id(sns_message)

        print(json.dumps({
            "step": "received_alarm",
            "alarm": alarm_name,
            "state": new_state,
            "instance_id": instance_id,
            "timestamp": timestamp
        }))

        if instance_id:
            # Tag the instance
            ec2.create_tags(
                Resources=[instance_id],
                Tags=[
                    {'Key': 'HighCPU', 'Value': 'true'},
                    {'Key': 'LastAlarm', 'Value': alarm_name},
                    {'Key': 'AlarmTime', 'Value': timestamp}
                ]
            )
            print(json.dumps({"step": "tagged_instance", "instance_id": instance_id}))

        # Write audit log to S3
        audit_record = {
            "event_type": "CPU_ALARM",
            "alarm_name": alarm_name,
            "alarm_state": new_state,
            "instance_id": instance_id,
            "action_taken": "ec2_tagged",
            "timestamp": timestamp,
            "raw_message": sns_message
        }

        s3_key = f"alarms/{alarm_name}/{timestamp.replace(':', '-')}.json"
        s3.put_object(
            Bucket=AUDIT_BUCKET,
            Key=s3_key,
            Body=json.dumps(audit_record, indent=2),
            ContentType='application/json'
        )
        print(json.dumps({"step": "audit_written", "s3_key": s3_key}))

    return {'statusCode': 200}

def extract_instance_id(message):
    """Extract EC2 instance ID from CloudWatch alarm dimensions."""
    try:
        dimensions = message['Trigger']['Dimensions']
        for dim in dimensions:
            if dim['name'] == 'InstanceId':
                return dim['value']
    except (KeyError, TypeError):
        pass
    return None