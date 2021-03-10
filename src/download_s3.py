import os
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto import s3
import boto3
from boto import boto
from configparser import ConfigParser
import json

import configparser
import os.path
from os import path


config_parser = configparser.ConfigParser()
config_parser.read("credentials.ini")
BUCKET_NAME = config_parser['MAIN']['BUCKET_NAME']

cred = boto3.Session().get_credentials()
ACCESS_KEY = cred.access_key
SECRET_KEY = cred.secret_key

s3 = boto3.resource('s3', region_name='us-east-2')
bucket = s3.Bucket(BUCKET_NAME)

for my_bucket_object in bucket.objects.all():
    print(my_bucket_object)

s3client = boto3.client('s3', 
        aws_access_key_id = ACCESS_KEY, 
        aws_secret_access_key = SECRET_KEY, 
        region_name='us-east-2'
    )

response = s3client.get_object(Bucket=BUCKET_NAME,Key='myfile.json')
body = response['Body'].read()

json_obj = json.loads(body)
print(json_obj) 