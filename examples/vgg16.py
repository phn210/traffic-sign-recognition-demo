import numpy as np
import cv2 as cv
import tensorflow as tf
import Helper


def predict(model, img_path):
    HEIGTH = 64
    WIDTH = 64
    image_to_read = cv.imread(img_path)
    resize_image = cv.resize(image_to_read,(HEIGTH, WIDTH))
    np_image = np.reshape(resize_image, [1, HEIGTH, WIDTH,3])
    predictions = model.predict(np_image)
    return predictions


model = Helper.loadModel('./models/VGG16')
class_id = np.argmax(predict(model, './test/non-detect/00001.png')) + 1

print(Helper.getClassName(class_id))