import boto3

ec2 = boto3.client('ec2')

INSTANCE_ID = "i-0b35450b04aecbc4f"  

def lambda_handler(event, context):

    print("Auto-remediation triggered")

    response = ec2.reboot_instances(
        InstanceIds=[i-0b35450b04aecbc4f]
    )

    print(f"Reboot response: {response}")

    return {
        "status": "success",
        "action": "reboot",
        "instance": INSTANCE_ID
    }