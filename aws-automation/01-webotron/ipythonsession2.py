# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
s3
session.region_name
new_bucket = s3. create_bucket(Bucket='automatingawsthanh-newbucket')
new_bucket
new_bucket.upload_file('index.html', 'index.html', ExtraArgs={'ContentType':'text/html'})
policy = """
{
  "Version":"2012-10-17",
  "Statement":[
    {
      "Sid":"AddPerm",
      "Effect":"Allow",
      "Principal": "*",
      "Action":["s3:GetObject"],
      "Resource":["arn:aws:s3:::%s/*"]
    }
  ]
}
""" % new_bucket.name
policy
print(policy)
pol = new_bucket.Policy()
print(pol)
pol.put(Policy=policy)
policy
print(policy)
policy
policy = policy.strip()
print(policy)
policy
pol.put(Policy=policy)
ws = new_bucket.Website()
ws.put(WebsiteConfiguration={})
ws.put(WebsiteConfiguration={'ErrorDocument' : {
'Key': 'error.html'
},
'IndexDocument': {
'Suffix': 'index.html'
}})
url = "https://%s.s3-website.us-east-1.amazonaws.com
url = "https://%s.s3-website.us-east-1.amazonaws.com"
url
url = "https://%s.s3-website.us-east-1.amazonaws.com" %new_bucket.name
url
url = "http://%s.s3-website.us-east-1.amazonaws.com" %new_bucket.name
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'ipythonsession2.py 1-32')
