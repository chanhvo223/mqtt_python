import paho.mqtt.client as mqtt_Client
import random
import time
import json
from datetime import date 

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Client is connected!")
        global connected 
        connected = True
    else:
        print("Connection is Failed!")

connected = False

broker_address = "103.149.253.133"
port = 49155
user = ""
password = ""

client = mqtt_Client.Client("Temparature")
client.username_pw_set(user, password= password)
client.on_connect = on_connect
client.connect(broker_address,port=port)

today = date.today()

client.loop_start()
while connected != True:
    time.sleep(0.5)
while True:
    # Tempatarure = round(random.uniform(10,40),2)
    # x = {
    #     "timeStamp" : today,
    #     "NameDevie" : "TempatarureDevice",
    #     "Value" : Tempatarure
    # }

    x = {
    "Qua1": {
        "voltage_1": 219.2,
        "voltage_2": 220.0,
        "voltage_3": 220.9,
        "power_1": 0,
        "power_2": 0,
        "power_3": 0,
        "current_1": 0,
        "current_2": 0,
        "current_3": 0,
        "energy": 0.8,
        "frequency": 50.06,
        "pf_1": 1,
        "pf_2": 1,
        "pf_3": 1,
        "rssi_wifi": -55
        }
    }
    payload = json.dumps(x)
    client.publish("mqtt/Temperature", payload=payload)
    time.sleep(3)
    print(type(str(x)))
    client.loop_stop()
