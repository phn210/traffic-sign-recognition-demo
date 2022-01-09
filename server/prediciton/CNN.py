import numpy as np
import cv2 as cv
import tensorflow as tf


def predict(model, img_path):
    total_classes = 43
    height = 32
    width = 32
    image_to_read = cv.imread(img_path)
    resize_image = cv.resize(image_to_read,(height, width))
    np_image = np.reshape(resize_image, [1, 32,32,3])
    predictions = model.predict(np_image)
    print(predictions)
    for i in range(total_classes):
        if predictions[0][i] > 0.01:
            return (i+1)
    return 0