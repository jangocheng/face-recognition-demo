#-*-coding:utf-8-*-
import face_recognition
import cv2
import mysql.connector

# 接入数据库
conn = mysql.connector.connect(user= 'root', password= '123456', host='127.0.0.1',database = 'face_library')
cursor = conn.cursor()
cursor.execute("SELECT * FROM face_table")
faces = cursor.fetchall()

# 开启摄像头
#video_capture = cv2.VideoCapture("rtsp://admin:jsptpd123456@172.16.9.251")
video_capture = cv2.VideoCapture(0)
# 初始化已有人脸列表
known_face_encodings = []
known_face_names =[]

def AddFace(name,image):
    name_image = face_recognition.load_image_file(image)
    name_face_encoding = face_recognition.face_encodings(name_image)[0]
    known_face_encodings.append(name_face_encoding)
    known_face_names.append(name)

# 将数据库中人脸导入
for face in faces:
    AddFace(face[1],face[2])

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # 抓取视频的单个画面
    ret, frame = video_capture.read()
    # 将图像由 BGR(OpenCV 使用) 转为RGB(face_recognition使用)
    rgb_frame = frame[:, :, ::-1]

    #每个画面一个进程来节省时间
    if process_this_frame:
        # 在当前画面找出所有人脸以及人脸编码
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        face_names = []

        for face_encoding in face_encodings:
            # 将检测到的人脸和人脸库进行比对检索
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, 0.47)
            name = "Unknown"
            # 若检测到匹配的人脸
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # 给捕捉到的图像画框
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    # 显示结果图像
    cv2.imshow('Video', frame)
    # 输出检测到的人脸
    print(face_names)

    # 按q键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放捕捉
video_capture.release()
# 清空所有窗口
cv2.destroyAllWindows()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()