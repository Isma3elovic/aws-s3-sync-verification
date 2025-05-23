📂 AWS S3 Sync & Verification with SNS Alerts

This project automates syncing files from multiple local directories to an AWS S3 bucket using the AWS CLI, and verifies the upload using a Python script. It also sends email alerts via AWS SNS if any file is missing from the bucket.

🚀 Features

Sync files to S3 using aws s3 sync

Verify S3 vs local files with a Python script

Send email alerts via SNS if discrepancies are found

Schedule automated verification with cron

🔧 Prerequisites

AWS CLI configured (aws configure)

Python 3.x

boto3 Python library

An S3 bucket created

IAM user with necessary permissions

🔐 IAM Setup

Create an IAM User

Enable Programmatic access

Attach a custom policy:

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket",
        "s3:GetObject",
        "sns:Publish"
      ],
      "Resource": "*"
    }
  ]
}

Configure AWS CLI

aws configure

Provide the IAM user's Access Key and Secret Key.

☁️ Sync Files to S3

Use the following command to sync local directories to your S3 bucket:

aws s3 sync /path/to/local/directory s3://your-bucket-name --delete

You can create a cron job to run this regularly (optional).

📬 SNS Setup

Create an SNS Topic in the AWS Console (e.g., FileSyncAlerts)

Subscribe your email to the topic

Confirm the subscription via the email you receive

Add the SNS Topic ARN to the Python script

🐍 Python Verification Script

This script:

Lists all local files

Lists all files in the S3 bucket

Compares both

Sends an SNS alert if any file is missing from S3

Make sure to install boto3:

pip install boto3

Example command to run:

python3 verify_s3_upload.py

🵒 Schedule with Cron (Optional)

To run the verification script at a specific time:

crontab -e

Add a line like this to run it every day at 1 AM:

0 1 * * * /usr/bin/python3 /path/to/verify_s3_upload.py


📩 Contact / Contribution

PRs are welcome! If you find this useful or want to improve it, feel free to contribute.

