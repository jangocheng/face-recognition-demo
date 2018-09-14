import requests
from json import JSONDecoder

try:
    http_url ="https://api-cn.faceplusplus.com/facepp/v3/compare"
    key ="1Fvlr9BTd7BKVR1kN3pYfWzsoJTIqnJm"
    secret ="6K9kMqHn-Rt5YxQDo0yd1z3cDOU4lO12"
    filepath1 = r"D:\python\faceplusplus\facelibrary\face1.jpg"
    filepath2 = r"D:\python\faceplusplus\facelibrary\face8.jpg"

    data = {"api_key":key, "api_secret": secret}
    files = {"image_file1": open(filepath1, "rb"),"image_file2": open(filepath2, "rb")}

    response = requests.post(http_url, data=data, files=files)

    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)

    confidence = req_dict['confidence']
    print("图片相似度：",confidence)

except Exception:
    print("无法识别！")