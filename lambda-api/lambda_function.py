import json
import uuid


def lambda_handler(event, context):
    # Log the incoming request to CloudWatch Logs
    print("Received data:", event.get("body"))

    # Generate a random ID for the submission
    submission_id = uuid.uuid4().hex[:8]

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "message": "Data successfully received and logged!",
            "id": submission_id
        })
    }
