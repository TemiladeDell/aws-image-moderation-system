**AWS Image Moderation System**
This project is part of my AWS learning journey. It uses Amazon Rekognition, AWS Lambda, Amazon S3, and CloudWatch Logs to automatically moderate images uploaded to an S3 bucket, detecting potentially unsafe or inappropriate content.

**What It Does**
Whenever a .jpg image is uploaded to a specific S3 bucket:

The upload triggers a Lambda function.

The function calls Amazon Rekognition to detect moderation labels (e.g., nudity, violence).

The moderation labels and confidence scores are printed to CloudWatch Logs.

(Optional/future enhancement) The system can be extended to send alerts or prevent access based on detected content.

**Technologies Used**
Amazon Rekognition – for automated moderation label detection

AWS Lambda – serverless compute for image processing logic

Amazon S3 – stores uploaded images and triggers the Lambda

Amazon CloudWatch Logs – logs the moderation results for visibility and debugging

**Project Structure**

Image-moderation/
├── moderate_image.py        # Lambda function source code
├── function.zip             # Zipped Lambda deployment package
├── .gitignore               # Standard Git ignore file
├── README.md                # Project documentation


**Setup Instructions**
Create an S3 bucket and enable event notifications for .jpg uploads to trigger a Lambda function.

Create the Lambda function with appropriate IAM permissions for Rekognition and S3 access.

**Package your Lambda function:**
zip function.zip moderate_image.py
**Deploy via CLI:**

aws lambda update-function-code \
  --function-name your-lambda-function-name \
  --zip-file fileb://function.zip


**Upload a test image:**
aws s3 cp your-image.jpg s3://your-bucket-name/
Check CloudWatch Logs for the moderation labels and confidence scores.

IAM Permissions
Ensure your Lambda execution role includes the following permissions:

rekognition:DetectModerationLabels

s3:GetObject

logs:CreateLogGroup

logs:CreateLogStream

logs:PutLogEvents


**Learning Outcomes**
Gained hands-on experience integrating multiple AWS services

Learned to use Amazon Rekognition for safe content detection

Practiced deploying and updating Lambda functions using the AWS CLI

Improved understanding of IAM roles, CloudWatch Logs, and S3 triggers


**Future Improvements**
Integrate Amazon SNS to send alerts when unsafe content is detected

Store moderation results in DynamoDB for analysis or auditing

Add web-based moderation dashboard or notification system

Author
Temilade Dell
[Medium](https://medium.com/@temiladedell) |  [LinkedIn](www.linkedin.com/in/temilade-akinyimika-dell001)
