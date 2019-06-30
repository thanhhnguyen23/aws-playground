# coding: utf-8
import boto3

# establishing session with profile
session = boto3.Session(profile_name='pythonAutomation')

# establishing session with s3
s3 = session.resource('s3')

# iterate through buckets
for bucket in s3.buckets.all():
    print(bucket)
    
# establishing session with ec2
ec2_client = session.client('ec2')

#ec2_client.allocate_address
#ec2_client.allocate_hosts
