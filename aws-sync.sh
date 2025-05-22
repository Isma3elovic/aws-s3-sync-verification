#!/bin/bash

# Sync local directory to S3 bucket
aws s3 sync /home/ubuntu/sync s3://asynce 

# Check if sync was successful
if [ $? -eq 0 ]; then
  echo "Sync completed successfully."
else
  echo "Sync failed!" >&2
  exit 1
fi
