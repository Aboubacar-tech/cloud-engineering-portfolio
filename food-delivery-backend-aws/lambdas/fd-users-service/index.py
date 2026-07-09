import json
import boto3
import uuid

dynamodb = boto3.resource("dynamodb")
table    = dynamodb.Table("users-table")

def lambda_handler(event, context):
    print("Event:", json.dumps(event))
    method      = event["httpMethod"]
    path        = event.get("path", "")
    path_params = event.get("pathParameters") or {}
    body_raw    = event.get("body") or "{}"

    try:
        body = json.loads(body_raw)
    except Exception:
        return respond(400, {"error": "Invalid JSON body"})

    # GET /users — scan all users
    if method == "GET" and path == "/users":
        result = table.scan()
        return respond(200, {"users": result["Items"]})

    # POST /users — create a new user
    if method == "POST" and path == "/users":
        name  = body.get("name")
        email = body.get("email")
        if not name or not email:
            return respond(400, {"error": "name and email are required"})
        user_id = str(uuid.uuid4())
        item = {"userId": user_id, "name": name, "email": email}
        table.put_item(Item=item)
        return respond(201, {"message": "User created", "user": item})

    # GET /users/{id}
    if method == "GET" and path_params.get("id"):
        result = table.get_item(Key={"userId": path_params["id"]})
        user   = result.get("Item")
        if not user:
            return respond(404, {"error": "User not found"})
        return respond(200, {"user": user})

    # PUT /users/{id}
    if method == "PUT" and path_params.get("id"):
        uid  = path_params["id"]
        name = body.get("name")
        if not name:
            return respond(400, {"error": "name is required"})
        table.update_item(
            Key={"userId": uid},
            UpdateExpression="SET #n = :name",
            ExpressionAttributeNames={"#n": "name"},
            ExpressionAttributeValues={":name": name},
        )
        return respond(200, {"message": "User updated"})

    # DELETE /users/{id}
    if method == "DELETE" and path_params.get("id"):
        table.delete_item(Key={"userId": path_params["id"]})
        return respond(200, {"message": "User deleted"})

    return respond(404, {"error": "Route not found"})

def respond(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }