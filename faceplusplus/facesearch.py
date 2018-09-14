#-*-coding:utf-8-*-
import cv2
import requests
import json

http_url ="https://api-cn.faceplusplus.com/facepp/v3/search"
key ="1Fvlr9BTd7BKVR1kN3pYfWzsoJTIqnJm"
secret ="6K9kMqHn-Rt5YxQDo0yd1z3cDOU4lO12"
filepath1 = r"D:\python\faceplusplus\facelibrary\face1.jpg"

data = {"api_key":key, "api_secret": secret,"outer_id":1}
files = {"image_file": open(filepath1, "rb")}
cap = cv2.VideoCapture(0)

imglib = {'ec5f6297ed378d96097b4f02d7d9fffa':'董',
          'c49848820faf45b1b3d916f5250c7d89':'鞠',
          'ef243b455ed5b0d57f5232d6b0d9e488':'陈',
          '1598429176a4712139f651ab86296342':'C罗',
          '3d54e61832189a09ab5aa8f6eb9af16d':'内马尔'}
while True:
    ret, frame = cap.read()
    cv2.imshow("capture", frame)
    cv2.imwrite(r"D:\python\faceplusplus\facelibrary\face1.jpg", frame)
    files = {"image_file": open(filepath1, "rb")}

    response = requests.post(http_url, data=data, files=files)
    req_dict = json.loads(response.text)
    print(req_dict)
    if req_dict['faces']:
        width =[]
        top = []
        height = []
        left = []
        img = cv2.imread(r"D:\python\faceplusplus\facelibrary\face1.jpg")
        vis = img.copy()
        for i in range(len(req_dict['faces'])):
            width.append(req_dict['faces'][i]['face_rectangle']['width'])
            top.append(req_dict['faces'][i]['face_rectangle']['top'])
            left.append(req_dict['faces'][i]['face_rectangle']['left'])
            height.append(req_dict['faces'][i]['face_rectangle']['height'])
            cv2.rectangle(vis, (left[i], top[i]), (left[i] + width[i], top[i] + height[i]), (0, 255, 0), 2)
        cv2.imshow("Image", vis)
        if req_dict['results']:
            if req_dict['results'][0]['confidence'] > 75:
                print("身份确认是：", imglib[req_dict['results'][0]['face_token']])
        else:
            print("未搜索到对应身份")
    else :
        print("未检测到人脸")
    cv2.waitKey(5)