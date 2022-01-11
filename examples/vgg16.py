import numpy as np
import cv2 as cv
import tensorflow as tf
import Helper


def predict(model, img_path):
    total_classes = 43
    height = 64
    width = 64
    image_to_read = cv.imread(img_path)
    resize_image = cv.resize(image_to_read,(height, width))
    np_image = np.reshape(resize_image, [1, 64,64,3])
    predictions = model.predict(np_image)
    return predictions


my_model = Helper.load_model('./CNN/model')
prediction = predict(my_model, './test/00001.png')

print(prediction)