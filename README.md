# Serverless Architecture Cloud Automation Assignment

## Assignment-1

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
   - **Runtime:** `Python 3.12`
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
- Python 3.12
