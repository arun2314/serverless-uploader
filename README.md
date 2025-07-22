Serverless File Storage – CI/CD with Jenkins
Project Overview
This project demonstrates a serverless file storage system using AWS Lambda, API Gateway, S3, and DynamoDB, with Jenkins set up for continuous integration and deployment (CI/CD).

The system allows users to upload files via an API. Files are stored in Amazon S3, and file metadata (like file name, size, and timestamp) is recorded in DynamoDB automatically.

Architecture
Postman Client sends a file via HTTP POST.

API Gateway triggers the uploadFileHandler Lambda function.

Lambda:

Saves the uploaded file in the S3 bucket (my-file-storages).

Stores metadata in the DynamoDB table (FileMetadata).

Jenkins CI/CD Pipeline:

Automatically updates the Lambda function code when changes are pushed to the GitHub repo.

AWS Resources Used
AWS Lambda – Function: uploadFileHandler

Amazon S3 – Bucket: my-file-storages

Amazon DynamoDB – Table: FileMetadata

Amazon API Gateway – API: FileUploadAPI

How It Works
Upload a file to the API endpoint using Postman:

Method: POST

Headers:

Content-Type: application/pdf

file-name: sample.pdf

Body: Binary file data

Lambda stores the file in S3 and metadata in DynamoDB.

Jenkins deploys new Lambda code automatically whenever you update the repository.

CI/CD Pipeline
Trigger: GitHub push → Jenkins pipeline starts.

Steps:

Pull the latest code from the repository.

Zip the Lambda function code.

Deploy the new code to AWS Lambda.

Testing
Use Postman to send a file upload request to your API Gateway endpoint:

arduino
Copy
Edit
https://r5hh1ovjc8.execute-api.us-east-1.amazonaws.com
Check the S3 bucket to confirm the file upload.

Verify DynamoDB for metadata entries.

Key Benefits
Fully serverless and scalable.

Automated deployments with Jenkins.

Easy to extend for larger file sizes and additional features.

Project Demo
A video demonstration of the entire workflow is included in the project.
