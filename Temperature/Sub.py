import paho.mqtt.client as mqtt_Client
import time 

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Client is connected!")
        global connected
        connected = True
        global messageReceived
        messageReceived = True
    else:
        print("Connection is failed!")

def on_message(client, userdata, message):
    print("Message receive" + str(message.payload.decode("utf-8")))
    # print("Topic" + str(message.topic))
    if message.retain == 1:
        print("This is a retained message!")


connected = False 
messageReceived = False

broker_address = "103.149.253.133"
port = 49155
user = ""
password = ""

client = mqtt_Client.Client("Temperature")
client.username_pw_set(username=user,password=password)
client.on_connect = on_connect
client.connect(broker_address,port=port)

client.loop_start()
while connected != True:
    time.sleep(0.5)
while messageReceived != True:
    time.sleep(0.5)
    print("w")
    time.sleep(5)
while  messageReceived == True:
    client.subscribe("PIOT/ConstrainedDevice/SensorMsg")
    client.on_message = on_message
    time.sleep(5)
client.loop_stop()



