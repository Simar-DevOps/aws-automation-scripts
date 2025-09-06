#!/usr/bin/env python3
import argparse, sys
import boto3
from botocore.exceptions import ClientError

def s3_client(region=None):
    return boto3.client("s3", region_name=region)

def list_buckets():
    s3 = s3_client()
    resp = s3.list_buckets()
    for b in resp.get("Buckets", []):
        print(b["Name"])

def create_bucket(bucket, region):
    s3 = s3_client(region)
    try:
        if region and region != "us-east-1":
            s3.create_bucket(Bucket=bucket,
                CreateBucketConfiguration={"LocationConstraint": region})
        else:
            s3.create_bucket(Bucket=bucket)
        print(f"✅ Created bucket: {bucket}")
    except ClientError as e:
        print(f"Create error: {e}")
        sys.exit(1)

def upload_file(bucket, path, key):
    s3 = s3_client()
    try:
        s3.upload_file(path, bucket, key)
        print(f"✅ Uploaded {path} → s3://{bucket}/{key}")
    except ClientError as e:
        print(f"Upload error: {e}")
        sys.exit(1)

def download_file(bucket, key, path):
    s3 = s3_client()
    try:
        s3.download_file(bucket, key, path)
        print(f"✅ Downloaded s3://{bucket}/{key} → {path}")
    except ClientError as e:
        print(f"Download error: {e}")
        sys.exit(1)

def list_objects(bucket, prefix=None):
    s3 = s3_client()
    params = {"Bucket": bucket}
    if prefix:
        params["Prefix"] = prefix
    try:
        resp = s3.list_objects_v2(**params)
        for obj in resp.get("Contents", []):
            print(obj["Key"], obj["Size"])
        if "Contents" not in resp:
            print("(bucket empty)")
    except ClientError as e:
        print(f"List error: {e}")
        sys.exit(1)

def main():
    p = argparse.ArgumentParser(description="S3 automation")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list-buckets")

    p_create = sub.add_parser("create-bucket")
    p_create.add_argument("--bucket", required=True)
    p_create.add_argument("--region", default="us-east-1")

    p_up = sub.add_parser("upload")
    p_up.add_argument("--bucket", required=True)
    p_up.add_argument("--path", required=True)
    p_up.add_argument("--key", required=True)

    p_down = sub.add_parser("download")
    p_down.add_argument("--bucket", required=True)
    p_down.add_argument("--key", required=True)
    p_down.add_argument("--path", required=True)

    p_list = sub.add_parser("list-objects")
    p_list.add_argument("--bucket", required=True)
    p_list.add_argument("--prefix", default=None)

    args = p.parse_args()

    if args.cmd == "list-buckets":
        list_buckets()
    elif args.cmd == "create-bucket":
        create_bucket(args.bucket, args.region)
    elif args.cmd == "upload":
        upload_file(args.bucket, args.path, args.key)
    elif args.cmd == "download":
        download_file(args.bucket, args.key, args.path)
    elif args.cmd == "list-objects":
        list_objects(args.bucket, args.prefix)

if __name__ == "__main__":
    main()
