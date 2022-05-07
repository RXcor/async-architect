import json
import pika

credentials = pika.credentials.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials, heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()

def publish(info, body, excange):
    info = json.dumps(info)
    properties = pika.BasicProperties(info)
    channel.basic_publish(
        exchange=excange, 
        routing_key="", 
        body=json.dumps(body), 
        properties=properties
    )