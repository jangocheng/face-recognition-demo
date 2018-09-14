#-*-coding:utf-8-*-
import requests
import json

http_url ="https://api-cn.faceplusplus.com/facepp/v3/detect"
key ="1Fvlr9BTd7BKVR1kN3pYfWzsoJTIqnJm"
secret ="6K9kMqHn-Rt5YxQDo0yd1z3cDOU4lO12"

filepath1 =r"D:\facepy\facerecognition\team\ju.jpg"

data = {"api_key":key, "api_secret": secret, "return_attributes": "gender,age,smiling,beauty"}
files = {"image_file": open(filepath1, "rb")}

response = requests.post(http_url, data=data, files=files)
req_dict = json.loads(response.text)
print(req_dict)