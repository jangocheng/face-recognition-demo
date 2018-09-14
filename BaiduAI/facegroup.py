from aip import AipFace
import base64

groupId = "group1"
APP_ID = '11507601'
API_KEY = 'UjWGYFG3My17yHWA6u3ME97V'
SECRET_KEY = 'vtKdKVRj2GBh7eER9VXb86PU0bjTnoG3'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)
""" 调用创建用户组 """
print(client.groupAdd(groupId))

with open("xxx.jpg", 'rb') as f:
    data = f.read()
    encodestr = base64.b64encode(data)
    image = str(encodestr, 'utf-8')

imageType = "BASE64"

groupId = "group1"

userId = "user1"

""" 调用人脸注册 """
print(client.addUser(image, imageType, groupId, userId))