
from kafka import KafkaProducer
import pandas as pd
import json

producer = KafkaProducer(
    bootstrap_servers='cheerful-glider-10705-us1-kafka.upstash.io:9092',
    sasl_mechanism='SCRAM-SHA-256',
    security_protocol='SASL_SSL',
    sasl_plain_username='Y2hlZXJmdWwtZ2xpZGVyLTEwNzA1JO3_r7aTmaaBDCAxw1EG9aaCdgX_eLFoWbQ',
    sasl_plain_password='ODgyZGI3YWQtYzMxYi00NmZlLWFmZWMtNDFhOWY5NjA4Njk4',
    api_version_auto_timeout_ms=100000
)

tracks = pd.read_csv('track.csv')

for dt in tracks.to_dict(orient='records'):
    data = json.dumps(dt).encode('utf-8')

    try:
        result = producer.send('artists', data).get(timeout = 60)    
        print("Message produced:", result)
    except Exception as e:
        print(f"Error producing message: {e}")
producer.close()