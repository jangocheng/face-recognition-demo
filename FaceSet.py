import json
import requests

def create(key, secret, kw=[]):
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/create"
    data = {"api_key" : key, "api_secret" : secret}
    data.update(kw)
    response = requests.post(http_url,data = data)

    req_dic = json.loads(response.text)
    print("Create FaceSet:",req_dic)
    return req_dic

def add(key, secret, faceset_token, face_tokens):
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/addface"
    data = {"api_key": key, "api_secret": secret, "faceset_token": faceset_token, "face_tokens": face_tokens}
    response = requests.post(http_url, data=data)

    req_dic = json.loads(response.text)
    print("Add face:",req_dic)
    return req_dic

def remove(key, secret, faceset_token, face_tokens):
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/removeface"
    data = {"api_key": key, "api_secret": secret, "faceset_token" : faceset_token, "face_tokens" : face_tokens}
    response = requests.post(http_url, data=data)

    req_dic = json.loads(response.text)
    print("Remove face:",req_dic)
    return req_dic

def update(key, secret, faceset_token, kw=[]):
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/update"
    data = {"api_key" : key, "api_secret" : secret, "faceset_token" : faceset_token}
    data.update(kw)
    response = requests.post(http_url,data = data)

    req_dic = json.loads(response.text)
    print("Update FaceSet:",req_dic)
    return req_dic

def delete(key, secret, kw=[]):
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/delete"
    data = {"api_key" : key, "api_secret" : secret}
    data.update(kw)
    response = requests.post(http_url,data = data)

    req_dic = json.loads(response.text)
    print("Delete FaceSet:",req_dic)
    return req_dic