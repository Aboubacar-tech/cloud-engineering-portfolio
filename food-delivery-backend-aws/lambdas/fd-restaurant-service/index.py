import json
import boto3
import uuid

dynamodb = boto3.resource("dynamodb")
restaurants = dynamodb.Table("restaurants-table")
menus = dynamodb.Table("menus-table")

def lambda_handler(event, context):
    method = event["httpMethod"]
    path = event.get("path", "")
    body = json.loads(event.get("body") or "{}")

    # GET all restaurants
    if method == "GET" and "/menu" not in path:
        return respond(200, restaurants.scan()["Items"])

    # GET menu
    if method == "GET" and "/menu" in path:
        restaurant_id = event["pathParameters"]["id"]

        response = menus.query(
            KeyConditionExpression=boto3.dynamodb.conditions.Key("restaurantId").eq(restaurant_id)
        )

        return respond(200, response["Items"])

    # POST restaurant
    if method == "POST":
        rid = str(uuid.uuid4())

        item = {
            "restaurantId": rid,
            "name": body["name"],
            "cuisine": body["cuisine"]
        }

        restaurants.put_item(Item=item)

        return respond(201, item)

    return respond(400, {"message": "Invalid request"})


def respond(status, body):
    return {
        "statusCode": status,
        "body": json.dumps(body)
    }