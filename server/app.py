from flask import Flask, request, jsonify, send_file, send_from_directory, safe_join, abort
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import os
from prediciton import Helper, CNN, VGG16, YOLO

UPLOAD_IMG_FOLDER = './uploads/images'
UPLOAD_VID_FOLDER = './uploads/videos'
ALLOWED_IMG_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'webp'}
ALLOWED_VID_EXTENSIONS = {'mp4', 'mov', 'wmv', 'gif', 'webm'}

app = Flask(__name__, static_folder='../client/build', static_url_path='')
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_IMG_FOLDER'] = UPLOAD_IMG_FOLDER
app.config['UPLOAD_VID_FOLDER'] = UPLOAD_VID_FOLDER


def allowed_file(filename, img):
    if img:
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_IMG_EXTENSIONS
    else:
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_VID_EXTENSIONS


# @app.route('/')
# @cross_origin()
# def home():
#     return {"notice": "welcome!!!"}


@app.route('/predict/img', methods=['POST'])
def process_image():
    response = {}
    if request.method == 'POST':
        image_path = ''
        class_name = ''
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            response["upload_result"] = "0"
            return response
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            print('No selected file')
            response["upload_result"] = "0"
            return response
        if file and allowed_file(file.filename, True):
            filename = secure_filename(file.filename)
            image_path = os.path.join(app.config['UPLOAD_IMG_FOLDER'], filename)
            file.save(image_path)
            response["upload_result"] = "1"
        else:
            print('test')
            response["upload_result"] = "0"

        # image_path = './test/images/00001.png'
        method = request.form['method']
        response['method'] = method
        if method == 'CNN':
            model = Helper.loadModel('./models/CNN/mymodelCV.h5')
            result = CNN.predict(model, image_path)
            if result > 0:
                class_name = Helper.getClassName(result)
                response['class_name'] = class_name
            else:
                response['class_name'] = ''

        elif method == 'VGG16':
            model = Helper.loadModel('./models/VGG16/')
            result = VGG16.predict(model, image_path)
            if result > 0:
                class_name = Helper.getClassName(result)
                response['class_name'] = class_name
            else:
                response['class_name'] = ''
            
        elif method == 'YOLO':
            weights_path = './models/YOLO/yolov3_training_last.weights'
            config_path = './models/YOLO/yolov3_training.cfg'
            # model = Helper.loadModel('./models/CNN/mymodelCV.h5')
            model = Helper.loadModel('./models/YOLO/traffic.h5')
            result = YOLO.predict_img(weights_path, config_path, model, image_path)
            class_names = []
            if len(result) > 0:
                for i in result:
                    class_names.append(Helper.getClassName(int(i)))
                response['class_name'] = class_names
            else:
                response['class_name'] = ''

        else:
            response['method'] = 0

        if image_path != '':
            os.remove(image_path)
    return response


@app.route('/')
@cross_origin
def serve():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    # cors = CORS(app)
    # app.run(debug=True)
    app.run()
