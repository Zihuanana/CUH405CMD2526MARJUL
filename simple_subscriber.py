import paho.mqtt.client as mqtt
import json
from datetime import date, datetime

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Subscriber connected successfully to Broker with result code:", rc)
        client.subscribe("mytopic/JT/sensors")
    else:
        print("Subscriberconnection failed with result code:", rc)

def on_message(client, userdata, msg):
    try:
        print("Subscriber received message on topic:", msg.topic)
        data = json.loads(msg.payload.decode("utf-8"))
        print(data)
    except json.JSONDecodeError:
        print("Subscriber cannot decode message on topic:", msg.topic)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Optional authentication
client.username_pw_set("AA", "qwerty")

# Connect to the broker and start listening
client.connect("broker.hivemq.com", 1883)
client.loop_forever()
