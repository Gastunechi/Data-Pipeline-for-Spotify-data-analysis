from kafka import KafkaConsumer
import pandas as pd
import json
import random
import string
import boto3
from io import StringIO


def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))
consumer = KafkaConsumer(
    'tracks',
    bootstrap_servers='cheerful-glider-10705-us1-kafka.upstash.io:9092',
    sasl_mechanism='SCRAM-SHA-256',
    security_protocol='SASL_SSL',
    sasl_plain_username='Y2hlZXJmdWwtZ2xpZGVyLTEwNzA1JO3_r7aTmaaBDCAxw1EG9aaCdgX_eLFoWbQ',
    sasl_plain_password='ODgyZGI3YWQtYzMxYi00NmZlLWFmZWMtNDFhOWY5NjA4Njk4',
    group_id='YOUR_CONSUMER_GROUP',
    auto_offset_reset='earliest'
)
# Initialize S3 client
s3_client = boto3.client('s3')

# Specify the S3 bucket and object key
bucket_name = 'de-project-kafka'

DATA = []
try:
    for message in consumer:
        DATA.append(json.loads(message.value))
        if len(DATA)>=10:
            df = pd.DataFrame(DATA)
            # df.to_csv('data.csv',index=False)
            csv_buffer = StringIO()
            df.to_csv(csv_buffer, index=False)
            s3_key = "staging/tracks/"+generate_random_string(20)+".csv"
            s3_client.put_object(Bucket=bucket_name, Key=s3_key, Body=csv_buffer.getvalue())
            print(f"DataFrame uploaded successfully to S3 bucket: {bucket_name} with key: {s3_key}")    
            DATA = []
except KeyboardInterrupt:
    pass
finally:
    consumer.close()