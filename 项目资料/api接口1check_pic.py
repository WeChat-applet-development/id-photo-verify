import requests
import base64
import json


url = 'http://apicall.id-photo-verify.com/api/check_pic'
pic = open('test.jpg', 'rb').read()
headers = {'Content-Type': 'application/json'}
data = {
    "spec_id": 23,
    "app_key": '1a3868f748d9c72652470529255295706a7598f2',
    "file": base64.b64encode(pic).decode()}
data_json = json.dumps(data)
response = requests.post(
    url=url,
    headers=headers,
    data=data_json)
print(response.text)
#print(base64.b64encode(pic).decode())