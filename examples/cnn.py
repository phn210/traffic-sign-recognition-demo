import numpy as np
import cv2 as cv
import Helper


def predict(model, img_path):
    total_classes = 43
    height = 32
    width = 32
    image_to_read = cv.imread(img_path)
    resize_image = cv.resize(image_to_read,(height, width))
    np_image = np.reshape(resize_image, [1, 32,32,3])
    predictions = model.predict(np_image)
    return predictions


model = Helper.loadModel('./models/CNN/mymodelCV.h5')
prediction = predict(model, './test/non-detect/00001.png')

for i in range(43):
    if prediction[0][i] == 1:
        print(Helper.getClassName(i+1))