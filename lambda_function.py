import boto3
import base64
import uuid
import datetime

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FileMetadata')

def lambda_handler(event, context):
    try:
        # Decode base64 file data
        file_data = base64.b64decode(event['body'])

        # Get file name from headers or use default
        file_name = event['headers'].get('file-name', f"{uuid.uuid4()}.bin")
        content_type = event['headers'].get('Content-Type', 'application/octet-stream')

        # Upload to S3
        s3.put_object(
            Bucket='my-file-storages',
            Key=file_name,
            Body=file_data,
            ContentType=content_type
        )

        # Store metadata in DynamoDB
        metadata = {
            'id': str(uuid.uuid4()),
            'file_name': file_name,
            'content_type': content_type,
            'uploaded_at': datetime.datetime.utcnow().isoformat()
        }
        table.put_item(Item=metadata)

        return {
            'statusCode': 200,
            'body': f"File {file_name} uploaded successfully."
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error uploading file: {str(e)}"
        }
