# 📂 AWS S3 Sync & Verification with SNS Alerts

This project automates syncing files from multiple local directories to an AWS S3 bucket using the AWS CLI. A Python script verifies uploads and sends alerts via SNS if any files are missing.

---

## 🚀 Features

- ✅ Sync files to S3 using `aws s3 sync`
- ✅ Verify S3 vs local files with Python
- ✅ Send email alerts via SNS if uploads fail
- ✅ Run sync & verification automatically via `cron`

---

## 🔧 Prerequisites

Before starting, ensure the following are installed and set up:

- AWS CLI
- Python 3.x
- `boto3` Python package
- S3 bucket created
- IAM user with proper permissions

---

## 🔐 IAM Setup

1. **Create IAM User**
   - Enable: **Programmatic access**
   - Create a custom policy with the following permissions:

     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Action": [
             "s3:ListBucket",
             "s3:GetObject",
             "s3:PutObject",
             "sns:Publish"
           ],
           "Resource": "*"
         }
       ]
     }
     ```

   - Attach this policy to your user and save the Access Key ID and Secret.

2. **Configure AWS CLI**

   Run this on your server:

   ```bash
   aws configure
Provide:

    Access Key ID

    Secret Access Key

    Default region (e.g. us-east-1)

    Default output format (json or leave blank)
    
☁️ S3 Sync Setup

You can use a bash script to sync local files to S3:
  ```bash
  #!/bin/bash
  aws s3 sync /home/ubuntu/sync s3://asynce --delete
```
Make the script executable:
```bash
chmod +x aws_sync.sh
```

📬 SNS Setup
```bash
    1- Create a Topic
    2- Go to the AWS SNS console, create a new topic (e.g., FileSyncAlerts), and copy the ARN.
    3- Subscribe an Email
    4- Click “Create subscription”
    5- Protocol: Email
    6- Endpoint: your-email@example.com
    7- Confirm the subscription from your inbox
    8- Update Script Configuration
    9- Add the topic ARN to your Python script for publishing alerts.
```

   🐍Python Verification Script

## 🐍 Install Python 3 (if not installed)

To check if Python 3 is installed:

```bash
python3 --version

sudo apt update
sudo apt install python3 python3-pip -y
python3 --version
pip3 --version
```

   Install dependencies:
```
   pip install boto3
```

Example usage:
```
python3 verify_s3_upload.py
```
Update the script with:

    Your bucket name

    Local directory path

    SNS topic ARN

    ```
