#-*-coding:utf-8-*-
import requests
import json

http_url ="https://api-cn.faceplusplus.com/facepp/v3/detect"
key ="your key"
secret ="your secret"

filepath1 =r"D:\python\facerecognition\facelibrary\face12.jpg"

data = {"api_key":key, "api_secret": secret, "return_attributes": "gender,age,smiling,beauty"}
files = {"image_file": open(filepath1, "rb")}

response = requests.post(http_url, data=data, files=files)
req_dict = json.loads(response.text)
print(req_dict)