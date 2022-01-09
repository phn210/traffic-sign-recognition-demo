import numpy as np
import cv2 as cv
import tensorflow as tf


def predict_img(weights_path, config_path, model, img_path):
    height = 32
    width = 32
    net = cv.dnn.readNet(weights_path, config_path)
    