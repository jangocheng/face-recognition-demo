import face_recognition
import cv2
import os
from urllib.request import urlretrieve

video_capture = cv2.VideoCapture(0)
known_face_encodings = []
known_face_names =[]


def save_img(img_url,file_name,file_path='img'):
    #保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的img文件夹
    try:
        if not os.path.exists(file_path):
            print('文件夹',file_path,'不存在，重新建立')
            #os.mkdir(file_path)
            os.makedirs(file_path)
        #获得图片后缀
        file_suffix = os.path.splitext(img_url)[1]
        #拼接图片名（包含路径）
        filename = '{}{}{}{}'.format(file_path,os.sep,file_name,file_suffix)
       #下载图片，并保存到文件夹中
        urlretrieve(img_url,filename=filename)
        return filename
    except IOError as e:
        print('文件操作失败',e)
    except Exception as e:
        print('错误 ：',e)

def AddFace(name,image,type = 'file'):
    if type=='url':
        image = save_img(image,name,file_path='img')
    name_image = face_recognition.load_image_file(image)
    name_face_encoding = face_recognition.face_encodings(name_image)[0]
    known_face_encodings.append(name_face_encoding)
    known_face_names.append(name)



AddFace("陈宇轩","http://localhost:8000/陈宇轩.jpg",'url')


face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # 抓取视频的单个画面
    ret, frame = video_capture.read()
    # 将画面调整成1/4来加快人脸识别速度
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # 将图像由 BGR(OpenCV 使用) 转为RGB(face_recognition使用)
    rgb_small_frame = small_frame[:, :, ::-1]

    # 每个画面一个进程来节省时间
    if process_this_frame:
        # 在当前画面找出所有人脸以及人脸编码
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)
    print(face_names)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()