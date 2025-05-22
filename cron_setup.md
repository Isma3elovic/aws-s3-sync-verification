# Sync files every day at 1 AM
0 1 * * * /path/to/aws_sync.sh

# Run verification script every day at 2 AM
0 2 * * * /usr/bin/python3 /path/to/sync_script.py
