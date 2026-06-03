import json
import boto3
import uuid

# Create Rekognition client
rekognition = boto3.client('rekognition')

# Create DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Connect to DynamoDB table
table = dynamodb.Table('ImageAnalysis')

# Main Lambda handler function
def lambda_handler(event, context):

    try:
        # Get S3 bucket name from event
        bucket = event['Records'][0]['s3']['bucket']['name']

        # Get uploaded image file name
        key = event['Records'][0]['s3']['object']['key']

        # Print bucket and file name in CloudWatch logs
        print("Bucket:", bucket)
        print("Image Key:", key)

        # Send image to Amazon Rekognition for label detection
        response = rekognition.detect_labels(
            Image={
                'S3Object': {
                    'Bucket': bucket,
                    'Name': key
                }
            },
            MaxLabels=10,        # Maximum labels to return
            MinConfidence=80     # Minimum confidence percentage
        )

        # Log successful Rekognition response
        print("Rekognition Success")

        # Extract label names from response
        labels = [label['Name'] for label in response['Labels']]

        # Store image details and labels in DynamoDB
        table.put_item(
            Item={
                'imageId': str(uuid.uuid4()),  # Generate unique ID
                'imageName': key,              # Store image name
                'labels': labels               # Store detected labels
            }
        )

        # Return successful response
        return {
            'statusCode': 200,
            'body': json.dumps(labels)
        }

    except Exception as e:
        # Log error message in CloudWatch
        print("Error:", str(e))

        # Return error response
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
