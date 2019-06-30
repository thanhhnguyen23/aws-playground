# 01 project

## pipenv
* setup environment for project and install boto3
```
pipenv --three
pipenv install boto3

# -d flag indicates will provide ipython in environment
pipenv install -d ipython
```

* must use command to run ipython in designated environment
```
pipenv run ipython
import boto3
```

## boto3
* python sdk
* boto3 is under aws command line
### create session to use aws configuration file
```
session = boto3.Session(profile_name='pythonAutomation')
```
### viewing s3 resources
* method 1
```
s3 = session.resource('s3')
for bucket in s3.buckets.all():
  print(bucket)
```
* method 2
```
aws s3 ls --profile pythonAutomation
```
### creating a s3 bucket via awscli
* method 1
```
new_bucket = s3.create_bucket(Bucket='automatingawsthanh-boto3')
```

* method 2
```
aws s3 mb s3://automatingthanh-commandline --profile pythonAutomation
```

### getting ec2 client
* method 1
```
ec2_client = session.client('ec2')
ec2.client.allocate_address
ec2.client.allocate_hosts

```
### view history with ipython
```
%history
```
### save history with ipython
```
%save ipythonsession.py 1-10
```

### running ipython from file
```
pipenv run ipython -i ipythonsession.py
```
## git
