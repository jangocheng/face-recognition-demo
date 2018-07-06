import requests
from json import JSONDecoder
import cv2

http_url ="https://api-cn.faceplusplus.com/facepp/v3/detect"
key ="your key"
secret ="your secret"

filepath1 =r"D:\xxx\face1.jpg"

data = {"api_key":key, "api_secret": secret, "return_attributes": "gender,age,smiling,beauty,emotion"}
files = {"image_file": open(filepath1, "rb")}
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("capture", frame)
    cv2.imwrite(r"D:\xxx\face1.jpg", frame)
    files = {"image_file": open(filepath1, "rb")}

    response = requests.post(http_url, data=data, files=files)

    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)

    width = req_dict['faces'][0]['face_rectangle']['width']
    top = req_dict['faces'][0]['face_rectangle']['top']
    left = req_dict['faces'][0]['face_rectangle']['left']
    height = req_dict['faces'][0]['face_rectangle']['height']

    img = cv2.imread(r"D:\xxx\face1.jpg")
    vis = img.copy()
    cv2.rectangle(vis, (left, top), (left + width, top + height), (0, 255, 0), 2)
    cv2.imshow("Image", vis)
    cv2.waitKey(5)