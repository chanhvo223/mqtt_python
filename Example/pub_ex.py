

import random
import time
import json

from paho.mqtt import client as mqtt_client


broker = '103.149.253.133'
port = 49155
topic = "mqtt/Temperature"
username = ''
password = ''

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client("mqtt")
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    while True:
        x = {
            "timeStamp": "2023-03-20T06:17:11.632090+00:00",
            "hasError": False,
            "name": "TempSensor",
            "typeID": 3,
            "statusCode": 0,
            "latitude": 0,
            "longitude": 0,
            "elevation": 0,
            "locationID": "constraineddevice001",
            "value": 25
                }
        payload = json.dumps(x)
        client.publish("mqtt/Temperature", payload=payload)
        time.sleep(5)
        print(type(x))

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()