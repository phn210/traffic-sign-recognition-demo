import numpy as np
import cv2
import tensorflow as tf

def predict(model, img_path):
    total_classes = 43
    height = 64
    width = 64
    image_to_read = cv2.imread(img_path)
    resize_image = cv2.resize(image_to_read,(height, width))
    np_image = np.reshape(resize_image, [1, 64,64,3])
    predictions = model.predict(np_image)
    for i in range(total_classes):
        if predictions[0][i] == 1:
            return (i+1)
    return -1