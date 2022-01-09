import numpy as np
import cv2
import tensorflow as tf

def load_model (model_path):
    CNN_MODEL = tf.keras.models.load_model(model_path)
    return CNN_MODEL

def predict(model, img_path):
    total_classes = 43
    height = 32
    width = 32
    image_to_read = cv2.imread(img_path)
    resize_image = cv2.resize(image_to_read,(height, width))
    np_image = np.reshape(resize_image, [1, 32,32,3])
    predictions = model.predict(np_image)
    return predictions

classes = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)', 
            3:'Speed limit (50km/h)', 
            4:'Speed limit (60km/h)', 
            5:'Speed limit (70km/h)', 
            6:'Speed limit (80km/h)', 
            7:'End of speed limit (80km/h)', 
            8:'Speed limit (100km/h)', 
            9:'Speed limit (120km/h)', 
            10:'No passing', 
            11:'No passing veh over 3.5 tons', 
            12:'Right-of-way at intersection', 
            13:'Priority road', 
            14:'Yield', 
            15:'Stop', 
            16:'No vehicles', 
            17:'Veh > 3.5 tons prohibited', 
            18:'No entry', 
            19:'General caution', 
            20:'Dangerous curve left', 
            21:'Dangerous curve right', 
            22:'Double curve', 
            23:'Bumpy road', 
            24:'Slippery road', 
            25:'Road narrows on the right', 
            26:'Road work', 
            27:'Traffic signals', 
            28:'Pedestrians', 
            29:'Children crossing', 
            30:'Bicycles crossing', 
            31:'Beware of ice/snow',
            32:'Wild animals crossing', 
            33:'End speed + passing limits', 
            34:'Turn right ahead', 
            35:'Turn left ahead', 
            36:'Ahead only', 
            37:'Go straight or right', 
            38:'Go straight or left', 
            39:'Keep right', 
            40:'Keep left', 
            41:'Roundabout mandatory', 
            42:'End of no passing', 
            43:'End no passing veh > 3.5 tons' }

my_model = load_model('./model/mymodelCV.h5')
prediction = predict(my_model, './test/00001.png')

for i in range(43):
    if prediction[0][i] == 1:
        print(f"Name of the sign is: {classes[i]}")