# 调用face++API的人脸识别demo
由于官方文档中Python的示例代码是2.* 版本，故自己写了个python3.6版本的小程序来试用学习。<br>
# Content
## facedetect.py
使用Opencv,通过摄像头捕捉人脸，返回的参数参考face++提供的API文档。<br>
如果只需要单张照片检测，把cv2相关的部分删掉即可。<br>
## facecompare.py
对两张人脸照片进行比对，判断是否是同一人，并返回置信系数。<br>
## facerecogniton.py(主要)
整合了前两个部分的功能。实现了摄像头检测人脸，并对库里的照片进行检索是否有对应的照片，从而返回对应的人名字。<br>
为了提高效率，采用了多线程来实现。<br>
<br>
# 使用方法
face++API帮助文档：https://console.faceplusplus.com.cn/documents/5671787 <br>
只需注册账号，向文件里填入对应的key和secret，自行修改图片路径，即可运行。<br>
