# Serverless File Storage – CI/CD with Jenkins

## Project Overview
This project is a **serverless file storage system** built with **AWS Lambda**, **Amazon API Gateway**, **S3**, and **DynamoDB**, using **Jenkins** for continuous integration and deployment (CI/CD).

Users can upload files through an API. Uploaded files go to an **S3 bucket**, and file metadata (file name, size, timestamp) is stored in **DynamoDB** automatically.

---

## Use of This Project

This project demonstrates how to build a **fully automated serverless file storage system** with CI/CD. It is useful for:

- **Learning Serverless Architecture**: Understand how AWS Lambda, API Gateway, S3, and DynamoDB work together.
- **Practicing CI/CD**: Gain hands-on experience setting up Jenkins pipelines that automatically deploy Lambda functions.
- **Building Scalable Storage Solutions**: Store and manage files without managing servers.
- **Portfolio Project**: Showcase real-world DevOps and cloud skills to employers.
- **Rapid Prototyping**: Quickly build backend file storage for apps without worrying about infrastructure.


## Architecture
- **Postman Client** sends files via HTTP POST.
- **API Gateway** triggers the **uploadFileHandler** Lambda function.
- **Lambda**:
  - Saves uploaded files to the **S3 bucket** `my-file-storages`.
  - Writes metadata to the **DynamoDB table** `FileMetadata`.
- **Jenkins Pipeline**:
  - Automatically deploys updated Lambda code when changes are pushed to GitHub.

---

## AWS Resources
- **AWS Lambda** – Function: `uploadFileHandler`
- **Amazon S3** – Bucket: `my-file-storages`
- **Amazon DynamoDB** – Table: `FileMetadata`
- **Amazon API Gateway** – API: `FileUploadAPI`

---

## How It Works
1. Use **Postman** to send a POST request:
   - **Headers**:
     - `Content-Type`: `application/pdf`
     - `file-name`: `sample.pdf`
   - **Body**: Binary file data
2. Lambda stores the file in S3 and metadata in DynamoDB.
3. Jenkins redeploys Lambda automatically when you update the GitHub repository.

---

## CI/CD Pipeline Steps
1. Pulls the latest code from GitHub.
2. Creates a ZIP of the Lambda function.
3. Deploys the ZIP to AWS Lambda.

---

## Testing the Setup
- API Gateway URL:  
https://your-api-url.execute-api.your-region.amazonaws.com
- Send a file with Postman.
- Confirm the file appears in the `my-file-storages` bucket.
- Check `FileMetadata` table for metadata entries.

---

## Benefits
- **Serverless**: Scales automatically with demand.
- **CI/CD**: Jenkins ensures fast and reliable deployments.
- **Simple**: Easy to test and extend.

