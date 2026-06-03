# Smart Image Upload and Analysis using AWS

A scalable and serverless image analysis application built on AWS using Amazon S3, AWS Lambda, Amazon Rekognition, and Amazon DynamoDB. The application automatically analyzes uploaded images, detects objects and labels using AI-powered image recognition, and stores the results in a NoSQL database. The serverless architecture ensures high availability, automatic scaling, and minimal infrastructure management.

## 🚀 Features

* Upload images to Amazon S3
* Automatic image processing using AWS Lambda
* AI-powered object and label detection with Amazon Rekognition
* Store analysis results in Amazon DynamoDB
* Event-driven serverless architecture
* Execution monitoring using Amazon CloudWatch
* Secure access control with AWS IAM
* Highly scalable and cost-effective solution

---

## Architecture

```text
User Uploads Image
        │
        ▼
   Amazon S3 Bucket
        │
        ▼
   S3 Event Trigger
        │
        ▼
    AWS Lambda
        │
        ▼
 Amazon Rekognition
        │
        ▼
 Amazon DynamoDB
        │
        ▼
   Analysis Results
```

---

## Tech Stack

| Technology         | Purpose                           |
| ------------------ | --------------------------------- |
| Amazon S3          | Image Storage                     |
| AWS Lambda         | Serverless Processing             |
| Amazon Rekognition | Image Analysis & Object Detection |
| Amazon DynamoDB    | NoSQL Database                    |
| Amazon CloudWatch  | Monitoring & Logging              |
| AWS IAM            | Access Management                 |

---

## Workflow

### Step 1: Upload Image

User uploads an image to the S3 bucket.

### Step 2: Trigger Lambda

Amazon S3 automatically triggers the Lambda function.

### Step 3: Analyze Image

Lambda sends the image to Amazon Rekognition for analysis.

### Step 4: Detect Labels

Rekognition identifies objects and labels within the image.

### Step 5: Store Results

Detected labels are stored in DynamoDB along with image details.

### Step 6: Monitor Execution

CloudWatch logs provide execution and debugging information.

---

## Example Input

### Uploaded Image

```text
dog.jpg
```

---

## Example Rekognition Output

```json
[
  {
    "Name": "Dog",
    "Confidence": 99.8
  },
  {
    "Name": "Pet",
    "Confidence": 98.5
  },
  {
    "Name": "Animal",
    "Confidence": 97.4
  }
]
```

---

## Example DynamoDB Record

```json
{
  "imageId": "12345",
  "imageName": "dog.jpg",
  "labels": [
    "Dog",
    "Pet",
    "Animal"
  ]
}
```

---

## Security

* IAM-based access control
* Least-privilege permissions for Lambda functions
* Secure S3 bucket access
* CloudWatch logging and monitoring
* Controlled access to DynamoDB resources

---

## Benefits of Serverless Architecture

* No server management
* Automatic scaling
* Cost-effective pay-per-use pricing
* High availability
* Fast deployment and maintenance
* Reduced operational overhead

---

## Future Enhancements

* Face Detection
* Celebrity Recognition
* Text Detection from Images
* Content Moderation
* SNS Email Notifications
* API Gateway Integration
* Web Dashboard for Analysis Results
* Real-Time Image Analytics

---

## Author

**Harini G**

Built with AWS Serverless Services, Amazon Rekognition, and DynamoDB for intelligent image analysis and automated cloud-based processing.
