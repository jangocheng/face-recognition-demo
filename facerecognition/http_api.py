#-*- coding:utf-8 -*-
import face_recognition
from flask import Flask, jsonify, request, redirect

# 允许的图片格式
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

known_face_encodings = []
known_face_names = []


def allowed_file(filename):
    """

    :param filename:
    :return:
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    # Check if a valid image file was uploaded
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # The image file seems valid! Detect faces and return the result.
            result = SearchFace(file, 0.47)
            return result

    # If no valid image file was uploaded, show the file upload form:
    return '''
    <!doctype html>
    <title>人脸身份检测</title>
    <h1>上传一张照片，检测身份</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''

def AddFace(name,image):
    name_image = face_recognition.load_image_file(image)
    name_face_encoding = face_recognition.face_encodings(name_image)[0]
    known_face_encodings.append(name_face_encoding)
    known_face_names.append(name)

def SearchFace(image,tolerance):
    unknown_image = face_recognition.load_image_file(image)
    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

    names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        names.append(name)

    result = {'检测结果': names}
    return jsonify(result)
"""
AddFace("xxx","xxx.jpg")
AddFace("xxx","xxx.jpg")
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)