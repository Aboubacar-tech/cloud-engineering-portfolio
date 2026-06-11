import json
import boto3

s3_client = boto3.client("s3")
BUCKET    = "resto-compart"

def lambda_handler(event, context):
    body     = json.loads(event.get("body") or "{}")
    filename = body.get("filename")
    filetype = body.get("contentType", "application/octet-stream")

    if not filename:
        return respond(400, {"error": "filename is required"})

    # Generate a pre-signed URL valid for 5 minutes
    presigned_url = s3_client.generate_presigned_url(
        "put_object",
        Params={
            "Bucket":      resto-compart,
            "Key":         f"uploads/{filename}",
            "ContentType": filetype,
        },
        ExpiresIn=300,  # 300 seconds = 5 minutes
    )

    return respond(200, {
        "uploadUrl": presigned_url,
        "expiresIn": "5 minutes",
        "instructions": "PUT your file directly to this URL"
    })

def respond(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }