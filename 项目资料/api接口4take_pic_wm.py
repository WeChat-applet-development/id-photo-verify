from PIL import Image
import requests
import urllib
import io


url = 'http://apicall.id-photo-verify.com/api/take_pic_wm/9fd7e5266c7211e782ad00163e06132ablue3_wm'
file = io.BytesIO(urllib.request.urlopen(url).read())
img = Image.open(file)
img.show()