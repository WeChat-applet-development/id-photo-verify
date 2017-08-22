import requests
import urllib
import io
import json


url = 'http://apicall.id-photo-verify.com/api/take_cut_pic'
headers = {'Content-Type': 'application/json'}
data = {
    "file_name": 'b8fba12e835a11e782c100163e06132a88524blue2',
    "app_key": 'e9467d512da0492b4e8f21ab1b111862cc3067bd',}
data_json = json.dumps(data)
response = requests.post(
    url=url,
    headers=headers,
    data=data_json)
print(response.status_code)