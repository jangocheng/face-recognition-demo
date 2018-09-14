#-*-coding:utf-8-*-
import requests
import json
import cv2

http_url ="https://api-cn.faceplusplus.com/facepp/v3/detect"
key ="1Fvlr9BTd7BKVR1kN3pYfWzsoJTIqnJm"
secret ="6K9kMqHn-Rt5YxQDo0yd1z3cDOU4lO12"

filepath1 =r"D:\facepy\facerecognition\team\face1.jpg"

data = {"api_key":key, "api_secret": secret, "return_attributes": "gender,age,smiling,beauty"}
files = {"image_file": open(filepath1, "rb")}
cap = cv2.VideoCapture(0)

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
    else :
        print("未检测到人脸")
    cv2.waitKey(5)