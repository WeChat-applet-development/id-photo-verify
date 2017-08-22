import requests
import base64
import json


url = ' http://apicall.id-photo-verify.com/api/cut_pic'
pic = open('test.jpg', 'rb').read()
headers = {'Content-Type': 'application/json'}
data = {
    "spec_id": 360,
    "app_key": 'e9467d512da0492b4e8f21ab1b111862cc3067bd',
    "file": base64.b64encode(pic).decode()}
data_json = json.dumps(data)
response = requests.post(
    url=url,
    headers=headers,
    data=data_json)
print(response.text)