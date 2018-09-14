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
    if False:
        continue
    # 抓取视频的单个画面
    ret, frame = video_capture.read()
    # 将画面调整成1/4来加快人脸识别速度
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # 将图像由 BGR(OpenCV 使用) 转为RGB(face_recognition使用)
    rgb_small_frame = small_frame[:, :, ::-1]

    #每个画面一个进程来节省时间
    if process_this_frame:
        faces = []
        # 在当前画面找出所有人脸以及人脸编码
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
            # 将检测到的人脸和人脸库进行比对检索
            distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            min_face_distance = 1
            # 找出最匹配的目标
            global min_num
            for i, face_distance in enumerate(distances):
                if face_distance < min_face_distance :
                    min_face_distance = face_distance
                    min_num = i

            name = "Unknown"
            distance = 1
            # 若检测到匹配的人脸
            if min_face_distance < 0.47:
                name = known_face_names[min_num]
                distance = distances[min_num]
            '''
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
            '''
            result = {"name":name ,"distance":distance}
            faces.append(result)

    process_this_frame = not process_this_frame

    # 给捕捉到的图像画框
    for (top, right, bottom, left) in face_locations:
        # 将检测到的人脸大小放大回原本的尺寸
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 105, 65), 2)

    # 显示结果图像
    cv2.imshow('Video', frame)
    # 输出检测到的人脸
    # 检测到唯一人脸不在库中
    if len(faces)== 1 and faces[0]['name'] == 'Unknown':
        error_code = 1
    # 未检测到人脸
    elif not len(faces):
        error_code = 2
    else:
        error_code = 0

    results = {'error_code':error_code,'faces':faces}
    print(results)

    # 按q键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放捕捉
video_capture.release()
# 清空所有窗口
cv2.destroyAllWindows()

# 关闭连接
cursor.close()
conn.close()

