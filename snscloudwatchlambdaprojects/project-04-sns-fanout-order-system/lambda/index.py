import json
from datetime import datetime

def lambda_handler(event, context):
    for record in event['Records']:
        # SNS delivers the message as a string — parse it
        message_str = record['Sns']['Message']
        order = json.loads(message_str)

        order_id = order.get('order_id', 'unknown')
        customer = order.get('customer', 'unknown')
        items = order.get('items', [])
        total = order.get('total', 0)

        print(json.dumps({
            "action": "ORDER_RECEIVED",
            "order_id": order_id,
            "customer": customer,
            "item_count": len(items),
            "total_usd": total,
            "processed_at": datetime.utcnow().isoformat()
        }))

    return {'statusCode': 200, 'body': 'Order processed'}