import json
import pika

credentials = pika.credentials.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials, heartbeat=None, blocked_connection_timeout=300))
channel = connection.channel()

def publish(body, excange):
    channel.basic_publish(
        exchange=excange, 
        routing_key="", 
        body=json.dumps(body)
    )