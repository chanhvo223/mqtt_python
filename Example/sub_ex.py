import random
import json
from paho.mqtt import client as mqtt_client
import requests
from  datetime import datetime


broker = '103.149.253.133'
port = 49155
topic = "mqtt/Temperature"
# generate client ID with pub prefix randomly
username = ''
password = ''

def sendtoinflux(bien):
    url = "http://192.168.1.18:8086/write?db=prime2&precision=s"
    headers = {
        'Content-Type': 'text/plain'
    }
    # param
    locationID = bien['locationID']
    now = datetime.now()
    hour = int(now.strftime("%H"))
    if hour > 6 and hour <= 14:
        shift = "2"
        vdate = now.strftime("%d/%m/%Y") 
    elif hour > 14 and hour <=22:
        shift = "3"
        vdate = now.strftime("%d/%m/%Y") 
    else: 
        shift ="1"
        vdate = now.strftime("%d/%m/%Y")  
    typeID = bien["typeID"]
    hasError = bien["hasError"] 
    value = bien["value"]
    ts = int(datetime.timestamp(now))

# #"TempSensor,locationID=constraineddevice002,shirt=1,date=3/20/2023,typeID=3 hasError=false,value=25 1679293031"
    msgInflux = (f"TempSensor,locationID={locationID},shift={shift},date={vdate},typeID={typeID} hasError={hasError},value={value} {ts}")
    response = requests.request("POST", url, headers=headers, data=msgInflux)
    print(msgInflux)
def connect_mqtt() -> mqtt_client:
    def on_connect(client, username, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client("P2")
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client,username, msg):
        # print(f"{msg.payload.decode('utf-8')}")
        payload = msg.payload.decode('utf-8')
        payload_dict = json.loads(payload)
        sendtoinflux(payload_dict)

        # # print(type(msg.payload.decode('utf-8')))

        # #lấy 1 key trong dict 
        # data = json.loads(payload)["Qua1"].keys()
        # for index, key in enumerate(data):
        #     if index == 1:
        #         print(key)
        #################################


    client.subscribe(topic)
    client.on_message = on_message



def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()