#-*-coding:utf-8-*-
import cv2
import requests
from json import JSONDecoder
import threading

def compareimage(filepath1 ,filepath2):
    try:
        http_url ="https://api-cn.faceplusplus.com/facepp/v3/compare"
        key ="your key"
        secret ="your secret"

        data = {"api_key":key, "api_secret": secret}
        files = {"image_file1": open(filepath1, "rb"),"image_file2": open(filepath2, "rb")}

        response = requests.post(http_url, data=data, files=files)

        req_con = response.content.decode('utf-8')
        req_dict = JSONDecoder().decode(req_con)

        confidence = req_dict['confidence']
        print("图片相似度：",confidence)
        return confidence

    except Exception:
        print("无法识别！")
        return 0

def videocap():
    while True:
        try:
            ret, frame = cap.read()
            cv2.imshow("capture", frame)
            cv2.imwrite(r"D:\xxx\face1.jpg", frame)
            cv2.waitKey(5)
        except Exception:
            pass 

def comimg(x):
    while True:
        if compareimage(imagelibrary[x], r"D:\xxx\face1.jpg") > 75:
            print("身份确认是：", x)

imagelibrary ={"吴宣仪":r"D:\xxx\face2.jpg",
               "yamy":r"D:\xxx\face4.jpg",
                "胡歌":r"D:\xxx\face7.jpg",
               "梅西": r"D:\xxx\face9.jpg",
               "C罗": r"D:\xxx\face11.jpg",
               "内马尔": r"D:\xxx\face12.jpg"}

cap = cv2.VideoCapture(0)

threading.Thread(target=videocap).start()
for x in imagelibrary:
    threading.Thread(target=comimg, args=(x,)).start()
