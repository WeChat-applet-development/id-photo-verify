import requests
import base64
import json


url = 'http://apicall.id-photo-verify.com/api/cut_check_pic'
pic = open('test.jpg', 'rb').read()
headers = {'Content-Type': 'application/json'}
data = {
    "spec_id": 360,
    "app_key": 'cde9b1520b8000004b6ea78784d3cfabed260334',
    "file": base64.b64encode(pic).decode()}
data_json = json.dumps(data)
response = requests.post(
    url=url,
    headers=headers,
    data=data_json)
print(response.text)