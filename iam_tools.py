#!/usr/bin/env python3
import argparse, sys, json
import boto3
from botocore.exceptions import ClientError

# Create IAM client
iam = boto3.client("iam")

# Minimal EC2 start/stop policy
EC2_MIN_POLICY = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances",
        "ec2:DescribeInstanceStatus",
        "ec2:DescribeTags"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:StartInstances",
        "ec2:StopInstances"
      ],
      "Resource": "*"
    }
  ]
}

def create_user(username):
    try:
        iam.create_user(UserName=username)
        print(f"✅ Created user: {username}")
    except ClientError as e:
        if e.response["Error"]["Code"] == "EntityAlreadyExists":
            print(f"User {username} already exists.")
        else:
            print(f"❌ Create user error: {e}")
            sys.exit(1)

def put_inline_policy(username, policy_name, policy_doc):
    try:
        iam.put_user_policy(
            UserName=username,
            PolicyName=policy_name,
            PolicyDocument=json.dumps(policy_doc)
        )
        print(f"✅ Attached inline policy {policy_name} to {username}")
    except ClientError as e:
        print(f"❌ Attach policy error: {e}")
        sys.exit(1)

def create_access_key(username):
    try:
        resp = iam.create_access_key(UserName=username)
        ak = resp["AccessKey"]["AccessKeyId"]
        sk = resp["AccessKey"]["SecretAccessKey"]
        print("✅ Created access key. Save these NOW:")
        print(f"AccessKeyId: {ak}")
        print(f"SecretAccessKey: {sk}")
    except ClientError as e:
        print(f"❌ Create key error: {e}")
        sys.exit(1)

def delete_access_key(username, access_key_id):
    try:
        iam.delete_access_key(UserName=username, AccessKeyId=access_key_id)
        print(f"✅ Deleted key {access_key_id} for {username}")
    except ClientError as e:
        print(f"❌ Delete key error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="IAM automation tool")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_create = sub.add_parser("create-user")
    p_create.add_argument("--username", required=True)

    p_policy = sub.add_parser("attach-ec2-min")
    p_policy.add_argument("--username", required=True)
    p_policy.add_argument("--policy-name", default="Ec2MinimalStartStop")

    p_key = sub.add_parser("create-key")
    p_key.add_argument("--username", required=True)

    p_delkey = sub.add_parser("delete-key")
    p_delkey.add_argument("--username", required=True)
    p_delkey.add_argument("--access-key-id", required=True)

    args = parser.parse_args()

    if args.cmd == "create-user":
        create_user(args.username)
    elif args.cmd == "attach-ec2-min":
        put_inline_policy(args.username, args.policy_name, EC2_MIN_POLICY)
    elif args.cmd == "create-key":
        create_access_key(args.username)
    elif args.cmd == "delete-key":
        delete_access_key(args.username, args.access_key_id)

if __name__ == "__main__":
    main()
