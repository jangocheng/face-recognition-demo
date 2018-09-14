from socket import socket,AF_INET,SOCK_STREAM
import datetime
import faceFunc

class Worker():
    def __init__(self, id = "", server_ip = "", server_port = 0):
        self.id = id
        self.server_ip = server_ip
        self.server_port = server_port
        self.client = self.connect()
        self.in_message = ''
        self.out_message = ''

    def getId(self):
        return self.id

    def __del__(self):
        self.close()

    @staticmethod
    def log(*args):
        print(args)

    def connect(self):
        client = None
        try:
            client = socket(AF_INET, SOCK_STREAM)
            client.connect((self.server_ip, self.server_port))
        except Exception as e:
            self.log(datetime.datetime.now().__str__(), e)
        return client

    def write(self, message):
        self.out_message = message
        self.send()

    def read(self):
        self.in_message = str(self.client.recv(8192), encoding="utf8")

    def send(self):
        bytes_msg = bytes(self.out_message, encoding="utf8")
        if self.client != None:
            self.client.send(bytes_msg)
            self.log(datetime.datetime.now().__str__(), self.out_message)

    def close(self):
        if self.client != None:
            try:
                self.client.close()
            except Exception as e:
                self.log(datetime.datetime.now().__str__(), e)

    def Loop(self):
        rgb_frame = faceFunc.capture_img(0)
        known_face_encodings = faceFunc.init_known_encodings()
        known_face_names = faceFunc.init_known_names()
        while True:
            if self.in_message == 'work':
                """
                results = search_face(rgb_frame, known_face_encodings, known_face_names)
                self.write(results)
                人脸识别主体代码调用
                """
                self.write('')
                continue
            else:
                self.read()
                if self.in_message == None or self.in_message == 'wait':
                    continue
                elif self.in_message == 'config':
                    continue
                    """
                    人脸识别配置调用
                    """

    def run(self):
        return

if __name__ == '__main__':
    # 服务端的ip地址
    server_ip = '127.0.0.1'
    # 服务端socket绑定的端口号
    server_port = 20000
    uuid = "00001"
    worker = Worker(uuid, server_ip, server_port)
    worker.Loop()
