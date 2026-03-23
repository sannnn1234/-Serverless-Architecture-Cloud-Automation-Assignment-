# Serverless-Architecture-Cloud-Automation-Assignment

### Step 1: Create EC2 Instances

1. Go to **AWS Console → EC2 → Instances → Launch Instances**
2. Launch a `t2.micro` instance 
3. In the **Tags** section, add:
   - Key: `Action` | Value: `Auto-Stop`
4. Launch a **second** `t2.micro` instance and tag it:
   - Key: `Action` | Value: `Auto-Start`
```
![EC2 Architecture](https://raw.githubusercontent.com/sannnn1234/-Serverless-Architecture-Cloud-Automation-Assignment-/main/Assigment1/EC2.png)
```
---

### Step 2: Create the IAM Role for Lambda
1. Go to **IAM → Roles → Create Role**
2. Select **Trusted entity**: `AWS Service` → `Lambda`
3. Attach the policy: **`AmazonEC2FullAccess`**
4. Name the role: `LambdaEC2ManagerRole`
5. Click **Create Role**
---

### Step 3: Create the Lambda Function
1. Go to **Lambda → Create Function**
2. Choose **Author from scratch**
3. Settings:
   - Function name: `EC2AutoManager`
   - Runtime: **Python 3.12**
   - Execution role: **Use existing role** → `LambdaEC2ManagerRole`
4. Click **Create Function**
5. click **Deploy**
---
### Step 4: Configure Lambda
1. **Timeout**: Go to **Configuration → General Configuration** → set timeout to **30 seconds** 
2. Click **Deploy** 
---

### Step 5: Test the Function

1. click the **Test** tab
2. Create a new test event —`ec2S
3. Click **Test**
4. Check the **Execution results** 
   ```
  ![Execution Results](https://raw.githubusercontent.com/sannnn1234/-Serverless-Architecture-Cloud-Automation-Assignment-/main/Assigment1/Lambda_Status.png)
   ```
5. Go to **EC2 → Instances** 
   - The `Auto-Stop` instance is now `stopping` or `stopped`
   - The `Auto-Start` instance is now `pending` or `running`

---

**Region**: Make sure the `region_name` in the code matches the region where your EC2 instances live — it's a very common gotcha.

**Optional: Schedule with EventBridge** — once the manual test passes, you can automate it by adding an **EventBridge (CloudWatch Events) trigger** in the Lambda console with a cron expression like `cron(0 18 * * ? *)` to run every day at 6 PM UTC.

For your GitHub repo, create the file as `lambda_function.py` in the root — that's exactly what Lambda expects as the entry point with the default handler name `lambda_function.lambda_handler`.
