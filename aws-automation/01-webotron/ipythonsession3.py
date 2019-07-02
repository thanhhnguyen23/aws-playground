# coding: utf-8
session
bucket = automatingawsthanh-newbucket
bucket
bucket = automatingawsthanh-newbucket
bucket
get_ipython().run_line_magic('history', '')
session
automatingawsthanh-newbucket
bucket = automatingawsthanh-newbucket
bucket = 'automatingawsthanh-newbucket'
from botocore.exceptions import ClientError
try: 
    s3_bucket = s3.create_bucket(
        Bucket = bucket,
        CreateBucketConfiguration={'LocationConstraint':session.region_name})
except ClientError as e:
    print(e)
    
try: 
    s3_bucket = s3.create_bucket(
        Bucket = bucket,
        CreateBucketConfiguration={'LocationConstraint':session.region_name})
except ClientError as e:
    print(e.response)
    
    
try: 
    s3_bucket = s3.create_bucket(
        Bucket = bucket,
        CreateBucketConfiguration={'LocationConstraint':session.region_name})
except ClientError as e:
    print(e.response)
    
    
try: 
    s3_bucket = s3.create_bucket(
        Bucket = bucket,
        CreateBucketConfiguration={'LocationConstraint':session.region_name})
except ClientError as e:
    print(e.response)
    if e.response('Error']['Code'] == 'BucketAlreadyOwnedByYou':
        s3_bucket = s3.Bucket(bucket) 
try: 
    s3_bucket = s3.create_bucket(
        Bucket = bucket,
        CreateBucketConfiguration={'LocationConstraint':session.region_name})
except ClientError as e:
    print(e.response)
    if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
        s3_bucket = s3.Bucket(bucket)
    else:
        raise e
        
try: 
    s3_bucket = s3.create_bucket(
        Bucket = bucket
    )
except ClientError as e:
    print(e.response)
    if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
        s3_bucket = s3.Bucket(bucket)
    else:
        raise e
        
s3_bucket
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'ipythonsession3.py 1-20')
