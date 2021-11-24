# amqps://ahfrkbge:hpAd_RxbP9lQv0tfe7X-VDW0q-TnPJRs@woodpecker.rmq.cloudamqp.com/ahfrkbge
import pika, json

params = pika.URLParameters(
    "amqps://ahfrkbge:hpAd_RxbP9lQv0tfe7X-VDW0q-TnPJRs@woodpecker.rmq.cloudamqp.com/ahfrkbge")

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange="", routing_key="admin", body=json.dumps(body), properties=properties)
