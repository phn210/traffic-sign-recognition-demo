import numpy as np
import cv2 as cv
import Helper


def predict(model, img_path):
    HEIGHT = 32
    WIDTH = 32
    image_to_read = cv.imread(img_path)
    resize_image = cv.resize(image_to_read,(HEIGHT, WIDTH))
    np_image = np.reshape(resize_image, [1, HEIGHT, WIDTH,3])
    predictions = model.predict(np_image)
    return predictions


model = Helper.loadModel('./models/CNN/mymodelCV.h5')
class_id = np.argmax(predict(model, './test/non-detect/00001.png')) + 1

print(Helper.getClassName(class_id))