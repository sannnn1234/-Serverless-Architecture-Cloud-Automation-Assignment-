# Serverless Architecture Cloud Automation Assignment

## Assignment 1: Automated Instance Management Using AWS Lambda and Boto3

---

## Step 1: Create EC2 Instances

1. Go to **AWS Console → EC2 → Instances → Launch Instance**
2. Launch a `t2.micro` instance
3. In the **Tags** section, add:
   - **Key:** `Action`
   - **Value:** `Auto-Stop`
4. Launch a **second** `t2.micro` instance and tag it:
   - **Key:** `Action`
   - **Value:** `Auto-Start`

### EC2 Instances Setup
![EC2 Instances](https://raw.githubusercontent.com/sannnn1234/-Serverless-Architecture-Cloud-Automation-Assignment-/main/Assigment1/EC2.png)

---

## Step 2: Create the IAM Role for Lambda

1. Go to **IAM → Roles → Create role**
2. Select **Trusted entity**: `AWS Service`
3. Choose **Use case**: `Lambda`
4. Attach the policy:
   - `AmazonEC2FullAccess`
5. Name the role:
   - `LambdaEC2ManagerRole`
6. Click **Create role**

---

## Step 3: Create the Lambda Function

1. Go to **AWS Lambda → Create function**
2. Choose **Author from scratch**
3. Configure:
   - **Function name:** `EC2AutoManager`
   - **Runtime:** `Python 3.14`
   - **Execution role:** Use existing role → `LambdaEC2ManagerRole`
4. Click **Create function**
5. Add the Lambda code and click **Deploy**

---

## Step 4: Configure Lambda Function

1. Go to **Configuration → General configuration**
2. Set **Timeout** to `30 seconds`
3. Click **Save**
4. Click **Deploy**

---

## Step 5: Test the Lambda Function

1. Go to the **Test** tab
2. Create a new test event:
   - **Event name:** `ec2StartStopTest`
3. Click **Test**
4. Verify the **Execution results**

### Lambda Execution Output
![Lambda Execution Results](https://raw.githubusercontent.com/sannnn1234/-Serverless-Architecture-Cloud-Automation-Assignment-/main/Assigment1/Lambda_Status.png)

---

## Step 6: Verify EC2 Instance Status

1. Go to **EC2 → Instances**
2. Verify:
   - Instance tagged `Action=Auto-Stop` → **Stopped / Stopping**
   - Instance tagged `Action=Auto-Start` → **Running / Pending**

---

## Technologies Used
- AWS EC2
- AWS Lambda
- AWS IAM
- Python 3.14

------------------------------------------------------------------------

# Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

## Objective

Automate deletion of files older than **30 days** from an S3 bucket
using AWS Lambda and Boto3.

------------------------------------------------------------------------

# Architecture

S3 Bucket (Files Stored) ↓ AWS Lambda (Python + Boto3) ↓ Delete Files
Older Than 30 Days

------------------------------------------------------------------------

# Step 1: Create S3 Bucket

1.  Go to **AWS Console → S3**
2.  Click **Create Bucket**
3.  Example bucket name:

cleanup-file-bucket

4.  Upload multiple files.

Ensure: - Some files are **older than 30 days** - Some files are
**recent**

Screenshot

![S3 Files](https://raw.githubusercontent.com/sannnn1234/-Serverless-Architecture-Cloud-Automation-Assignment-/main/aws-s3-cleanup-lambda/screenshots/S3 BUCKET.png)

------------------------------------------------------------------------

# Step 2: Create IAM Role for Lambda

1.  Open **IAM → Roles**
2.  Click **Create Role**
3.  Select **Lambda**
4.  Attach policy:

AmazonS3FullAccess

5.  Role Name:

LambdaS3CleanupRole

Screenshot

![IAM Role](aws-s3-cleanup-lambda/screenshots/S3 Cleanup Role.png)

------------------------------------------------------------------------

# Step 3: Create Lambda Function

Configuration:

Function Name: S3BucketCleanup\
Runtime: Python 3.x\
Execution Role: LambdaS3CleanupRole

Screenshot

![Lambda Create](aws-s3-cleanup-lambda/screenshots/S3 Cleanup Lambda.png)

------------------------------------------------------------------------

# Step 4: Lambda Code

``` python
import boto3
from datetime import datetime, timezone, timedelta

s3 = boto3.client('s3')

BUCKET_NAME = "cleanup-file-bucket"
DAYS = 30

def lambda_handler(event, context):

    deleted_files = []

    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    if 'Contents' not in response:
        print("Bucket is empty")
        return

    for obj in response['Contents']:

        file_name = obj['Key']
        last_modified = obj['LastModified']

        file_age = datetime.now(timezone.utc) - last_modified

        if file_age > timedelta(days=DAYS):

            s3.delete_object(
                Bucket=BUCKET_NAME,
                Key=file_name
            )

            deleted_files.append(file_name)
            print(f"Deleted: {file_name}")

    if not deleted_files:
        print("No old files found")

    return {
        'statusCode': 200,
        'deleted_files': deleted_files
    }
```

Screenshot

![Lambda Code](aws-s3-cleanup-lambda/screenshots/lambda-code-s3.png)

------------------------------------------------------------------------

# Step 5: Test Lambda

1.  Click **Deploy**
2.  Click **Test**
3.  Create test event

Event Name: test

Screenshot

![Lambda Test](aws-s3-cleanup-lambda/screenshots/lambda-test-s3.png)

------------------------------------------------------------------------

# Step 6: Verify Results

After running Lambda:

  File Age             Result
  -------------------- ---------
  Older than 30 days   Deleted
  Newer than 30 days   Remains
