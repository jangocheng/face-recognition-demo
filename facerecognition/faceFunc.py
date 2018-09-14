#-*-coding:utf-8-*-
import face_recognition
import cv2
from urllib.request import urlretrieve
import os

def save_img(img_url,file_name,file_path='img'):
    '''
    保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的img文件夹
    :param img_url: 要保存的网络图片地址
    :param file_name:要保存的文件名
    :param file_path:保存到的文件目录地址
    :return:保存后的图片路径
    '''
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

def AddFace(name, image, known_face_encodings, known_face_names,type = 'file'):
    '''
    将库里的照片导入到比对时所用的编码集合与姓名集合
    :param name:要添加的人脸姓名
    :param image:要添加的人脸照片
    :param known_face_encodings:库里的人脸编码集合
    :param known_face_names: 库里人脸对应身份集合
    :param type:'url'为网络图片，'file'为本地图片，默认为本地图片
    :return:
    '''
    if type=='url':
        image = save_img(image,name,file_path='img')
    name_image = face_recognition.load_image_file(image)
    name_face_encoding = face_recognition.face_encodings(name_image)[0]
    known_face_encodings.append(name_face_encoding)
    known_face_names.append(name)



def capture_img(caddress = 0):
    '''
    调用Opencv库，捕捉摄像头画面，并将BGR图像(OpenCV使用)调整为RGB图像(face_recognition使用)
    :param caddress: 调用的摄像头地址
    :return:
    '''
    # video_capture = cv2.VideoCapture("rtsp://admin:jsptpd123456@172.16.9.251")
    video_capture = cv2.VideoCapture(caddress)
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]
    '''
    调整为1/4的画面进行识别，能够加快识别速度。
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    '''
    return rgb_frame

def init_known_encodings():
    '''
    初始化已有人脸编码集合
    :return: 已有人脸编码集合
    '''
    known_face_encodings = []
    return known_face_encodings

def init_known_names():
    '''
    初始化已有人脸身份集合
    :return: 已有人脸身份集合
    '''
    known_face_names = []
    return  known_face_names

def search_face(rgb_frame, known_face_encodings, known_face_names):
    '''
    使用face_Recognition进行人脸检索
    :param rgb_frame: 要进行检索的人脸图片
    :param known_face_encodings: 已有人脸编码集合
    :param known_face_names: 已有人脸身份集合
    :return: 比对结果
    '''
    faces = []
    # 在当前画面找出所有人脸以及人脸编码
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        # 将检测到的人脸和人脸库进行比对检索
        distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        min_face_distance = 1
        # 找出最匹配的目标
        global min_num
        for i, face_distance in enumerate(distances):
            if face_distance < min_face_distance:
                min_face_distance = face_distance
                min_num = i

        name = "Unknown"
        confidence = 100.00
        # 若检测到匹配的人脸
        if min_face_distance < 0.55:
            name = known_face_names[min_num]
            distance = distances[min_num]
            confidence = round((1-distance)*100,2)
        result = {"name": name, "confidence": confidence}
        faces.append(result)

    # 检测到唯一人脸不在库中
    if len(faces) == 1 and faces[0]['name'] == 'Unknown':
        error_code = 1
    # 未检测到人脸
    elif not len(faces):
        error_code = 2
    else:
        error_code = 0

    results = {'error_code': error_code, 'faces': faces}
    return results