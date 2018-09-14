# -*- coding: UTF-8 -*-
import base64
from aip import AipFace
import cv2

APP_ID = '11507601'
API_KEY = 'UjWGYFG3My17yHWA6u3ME97V'
SECRET_KEY = 'vtKdKVRj2GBh7eER9VXb86PU0bjTnoG3'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)
groupIdList = "group1"
imageType = "BASE64"
cap = cv2.VideoCapture(0)

""" 如果有可选参数 """
options = {}
options["face_field"] = "age"
options["max_face_num"] = 10
options["face_type"] = "LIVE"

while True:
    ret, frame = cap.read()
    cv2.imshow("capture", frame)
    cv2.imwrite(r"D:\python\faceplusplus\facelibrary\face1.jpg", frame)
    with open(r"D:\python\faceplusplus\facelibrary\face1.jpg", 'rb') as f:  # 以二进制读取图片
        data = f.read()
        encodestr= base64.b64encode(data)  # 得到 byte 编码的数据
        image = str(encodestr, 'utf-8')  # 重新编码数据
    response = client.detect(image, imageType, options)
    print("检测结果:",response)

    if response['error_msg']=='SUCCESS':
        width =[]
        top = []
        height = []
        left = []
        img = cv2.imread("xxx.jpg")
        vis = img.copy()
        for i in range(response['result']['face_num']):
            width.append(response['result']['face_list'][i]['location']['width'])
            top.append(response['result']['face_list'][i]['location']['top'])
            left.append(response['result']['face_list'][i]['location']['left'])
            height.append(response['result']['face_list'][i]['location']['height'])
            cv2.rectangle(vis, (int(left[i]), int(top[i])), (int(left[i] + width[i]), int(top[i] + height[i])), (0, 255, 0), 2)
        cv2.imshow("Image", vis)
    else :
        print("未检测到人脸")

    result = client.match([{'image': image,'image_type': 'BASE64'},
                       {'image': str(base64.b64encode(open(r'D:\python\faceplusplus\facelibrary\face10.jpg', 'rb').read()),'utf-8'),'image_type': 'BASE64'}])
    print("对比结果：",result)

    print("搜索结果:",client.search(image, imageType, groupIdList))

    cv2.waitKey(5)