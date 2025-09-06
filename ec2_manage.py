#!/usr/bin/env python3
import argparse
import sys
import boto3
from botocore.exceptions import ClientError

def ec2_client(region=None):
    return boto3.client("ec2", region_name=region)

def list_instances(region=None):
    ec2 = ec2_client(region)
    response = ec2.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            iid   = instance["InstanceId"]
            state = instance["State"]["Name"]
            pub   = instance.get("PublicIpAddress", "-")
            priv  = instance.get("PrivateIpAddress", "-")
            name  = "-"
            for t in instance.get("Tags", []) or []:
                if t["Key"] == "Name":
                    name = t["Value"]
            print(f"{iid}\t{state}\t{name}\t{pub}\t{priv}")

def start_instance(instance_id, region=None):
    ec2 = ec2_client(region)
    print(f"Starting {instance_id}...")
    ec2.start_instances(InstanceIds=[instance_id])
    waiter = ec2.get_waiter("instance_running")
    waiter.wait(InstanceIds=[instance_id])
    print(f"✅ {instance_id} is running.")

def stop_instance(instance_id, region=None):
    ec2 = ec2_client(region)
    print(f"Stopping {instance_id}...")
    ec2.stop_instances(InstanceIds=[instance_id])
    waiter = ec2.get_waiter("instance_stopped")
    waiter.wait(InstanceIds=[instance_id])
    print(f"✅ {instance_id} is stopped.")

def main():
    parser = argparse.ArgumentParser(description="Manage EC2 instances")
    parser.add_argument("action", choices=["list", "start", "stop"])
    parser.add_argument("--id", help="EC2 InstanceId")
    parser.add_argument("--region", default="us-east-1")
    args = parser.parse_args()

    try:
        if args.action == "list":
            list_instances(args.region)
        elif args.action == "start":
            if not args.id:
                print("❌ You must provide --id for start")
                sys.exit(1)
            start_instance(args.id, args.region)
        elif args.action == "stop":
            if not args.id:
                print("❌ You must provide --id for stop")
                sys.exit(1)
            stop_instance(args.id, args.region)
    except ClientError as e:
        print(f"AWS error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
