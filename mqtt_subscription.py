#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import traffic_light
def on_connect(client, userdata, flags, rc):
    # This will be called once the client connects
    print(f"Connected with result code {rc}")
    # Subscribe here!
    client.subscribe("traffic_status")
def on_message(client, userdata, msg):
    print(f"Message received [{msg.topic}]: {msg.payload}")
    traffic_light.lightcycle()
client = mqtt.Client("mqtt-test") # client ID "mqtt-test"
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("birol", "123456")
client.connect('127.0.0.1', 1883)
client.loop_forever()  # Start networking daemon
