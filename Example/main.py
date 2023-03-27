import requests

url = "http://192.168.1.18:8086/write?db=prime2&precision=s"

payload = "TempSensor,locationID=constraineddevice001,shirt=1,date=3/20/2023,typeID=3 hasError=false,value=25 1679293031"
headers = {
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)