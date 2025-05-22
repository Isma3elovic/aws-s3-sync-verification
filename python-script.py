import boto3
import os

# Config - Change these values
bucket_name = 'asynce'
local_folder = '/home/ubuntu/sync'
sns_topic_arn = 'arn:aws:sns:eu-west--00000000-:sync'

s3 = boto3.client('s3')
sns = boto3.client('sns')

def list_s3_files(bucket):
    keys = set()
    paginator = s3.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=bucket):
        for obj in page.get('Contents', []):
            keys.add(obj['Key'])
    return keys

def list_local_files(folder):
    files = set()
    for root, dirs, filenames in os.walk(folder):
        for fname in filenames:
            full_path = os.path.join(root, fname)
            relative_path = os.path.relpath(full_path, folder)
            files.add(relative_path.replace('\\','/'))
    return files

def notify_unsynced_files(missing_files):
    message = f"Files missing in S3 bucket {bucket_name}:\n" + "\n".join(missing_files)
    sns.publish(TopicArn=sns_topic_arn, Message=message, Subject="S3 File Sync Alert")

def main():
    s3_files = list_s3_files(bucket_name)
    local_files = list_local_files(local_folder)
    missing_files = local_files - s3_files
    if missing_files:
        notify_unsynced_files(missing_files)
        print(f"Notification sent for {len(missing_files)} files.")
    else:
        print("All files are synced to S3.")

if __name__ == "__main__":
    main()
