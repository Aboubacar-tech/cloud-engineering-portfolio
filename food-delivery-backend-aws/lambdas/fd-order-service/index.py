import json
import boto3
import uuid

dynamodb   = boto3.resource("dynamodb")
orders_t   = dynamodb.Table("orders-table")


def lambda_handler(event, context):
    print("Event:", json.dumps(event))
    method = event["httpMethod"]
    path   = event.get("path", "")
    params = event.get("pathParameters") or {}
    body   = json.loads(event.get("body") or "{}")

    # ── /orders ──────────────────────────────────────────
    if path == "/orders":
        if method == "GET":
            return respond(200, {"orders": orders_t.scan()["Items"]})
        if method == "POST":
            oid  = str(uuid.uuid4())
            item = {
                "orderId":   oid,
                "userId":    body.get("userId"),
                "productId": body.get("productId"),
                "quantity":  body.get("quantity", 1),
                "status":    "pending"
            }
            orders_t.put_item(Item=item)
            return respond(201, {"order": item})

    return respond(404, {"error": "Route not found"})

def respond(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }