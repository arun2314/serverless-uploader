import boto3
import base64
import json
import uuid
import datetime

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
bucket_name = 'my-file-storages'   # Your S3 bucket name
table_name = 'FileMetadata'        # We will create this table in Step 3

def lambda_handler(event, context):
    try:
        print("Jenkins is working — new deployment confirmed!")
        # Read file from API body (base64 encoded)
        file_content = base64.b64decode(event['body'])

        # Get filename and content-type from headers
        file_name = event['headers'].get('file-name', f'upload-{uuid.uuid4()}')
        content_type = event['headers'].get('content-type', 'application/octet-stream')

        # Upload to S3
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file_content,
            ContentType=content_type
        )

        # Save metadata to DynamoDB
        table = dynamodb.Table(table_name)
        table.put_item(
            Item={
                'id': str(uuid.uuid4()),
                'fileName': file_name,
                'contentType': content_type,
                'size': len(file_content),
                'uploadedAt': datetime.datetime.utcnow().isoformat()
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'File uploaded and metadata saved'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

