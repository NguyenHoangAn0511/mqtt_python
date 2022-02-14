import random
import string
from time import sleep
import paho.mqtt.client as mqtt


BROKER_URL = 'localhost'
PORT = 1883
TOPIC = 'hoangan/mqtt'


def random_string():
    output =  ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
    return output

def data_simulation():
    return str({
        'data': random_string(),
        'id': random_string(),
        'img': random_string()
    })


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(f"Connected to {BROKER_URL} with port {PORT} successfully!")
        else:
            print(f"Failed to connect, return code %d\n", rc)
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(BROKER_URL, PORT)
    return client


def publish(client):
    def on_publish(client, userdata, rc):
        print("Data published")
    while True:
        sleep(1)
        msg = data_simulation()
        result = client.publish(TOPIC, msg)
        client.on_publish = on_publish
        status = result[0]

        if status == 0:
            print(f"Send {msg} to {TOPIC}")
        else:
            print("Failed to send message to {TOPIC}")


def subscribe(client):
    def on_message(client, userdata, msg):
        print(f"Recieve {msg.payload.decode()} from {msg.topic}")
    
    client.subscribe(TOPIC)
    client.on_message = on_message