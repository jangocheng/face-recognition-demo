# 开源项目face_recognition
## content
* Face_Recognition.py
调用face_recognition库和opencv库，实现对web摄像头对人脸的动态检测搜索。<br>几个
* http_api.py
使用flask框架实现的一个简易的单张图片搜索人脸库的API。<br>
* face_rec_function.py
单独的函数<br><br>

## 使用方法
[GitHub地址](https://github.com/ageitgey/face_recognition)<br><br>

# 调用face++API
## Content
* facedetect.py
使用Opencv,通过摄像头捕捉人脸，返回的参数参考face++提供的API文档。<br>
* singilefacedetect.py
单张照片检测<br>
* facecompare.py
对两张人脸照片进行比对，判断是否是同一人，并返回置信系数。<br>
* facerecogniton.py
整合了前两个部分的功能。实现了摄像头检测人脸，并对库里的照片用字典进行检索是否有对应的照片，从而返回对应的人名字。<br>
为了提高效率，采用了多线程来实现。<br>
* facesearch.py
用摄像头检测尺寸最大的人脸，在创建的faceset中搜索找到是否有对应人脸。<br><br>

## 使用方法
face++API帮助文档：https://console.faceplusplus.com.cn/documents/5671787 <br>
只需注册账号，向文件里填入对应的key和secret，自行修改图片路径，即可运行。<br>
对于facesearch文件，需要先创建FaceSet，可运行CreateSet.py来创建，对FaceSet的各种操作，集中在了FaceSet.py中<br>
<br><br>

# BaiduAI
## Content
* baiduAI_face.py
使用了百度AI平台提供的人脸识别HTTP SDK<br>
调用实现了人脸检测，人脸比对和人脸检索，通过opencv摄像头检测人脸传入照片数据。<br>
* facegroup.py
创建了一个照片库，并向该照片库里加入一张人脸照片。库里的照片供人脸检索使用。<br><br>

## 使用方法
注册百度AI平台账号，填入自己的公钥和密钥即可使用。<br>
百度AI开放平台帮助文档：<br>
参考文档：[API文档](http://ai.baidu.com/docs#/Face-Detect-V3/top)，
[HTTP SDK文档](http://ai.baidu.com/docs#/Face-Python-SDK/top)<br>
<br><br>

# Microsoft Azure
## Content
* Azure_face.py
检测了一张含人脸的照片，并用PIL画出人脸框。<br><br>

## 使用方法
首先注册微软的认知服务平台账号，相比其他平台极其繁琐，需要上传身份证照片，以及充值一元来试用一个月。<br>
然后填入自己的KEY<br>
由于区分中国区和世界版，故在调用Url时需要修改为中国区的调用网址。<br>
参考文档：[人脸API文档](https://docs.azure.cn/zh-cn/cognitive-services/Face/)<br>