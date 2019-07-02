# running webotron
* method 1
pipenv run python webotron/webotron.py

* method 2
pipenv shell
python webostron/webotron.py

# webotron.py
```
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

```
# sys library
# click library

* click arguments
* click group

## 1. create bucket
## 2. add content aka website assets (html, css, js, jpg, and etc.)
## 3. make accessible to the public
## 4. turn on website hosting for s3 bucket

## find out which region are you using
session.region_name
