import numpy as np
import cv2 as cv
import time
import os
import Helper


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images


input_folder_path = "./test/detect/images/input"
output_folder_path = "./test/detect/images/output"
all_images = load_images_from_folder(input_folder_path)
print('Total Images: ',len(all_images))
HEIGHT = 32
WIDTH = 32

net = cv.dnn.readNet("./model/YOLO/yolov3_training_last.weights", "./models/YOLO/yolov3_training.cfg")

classes = Helper.getAllSignsName()

#get last layers names
layer_names = net.getLayerNames()
print(len(layer_names))
print(net.getUnconnectedOutLayers())
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))
check_time = True
confidence_threshold = 0.5
font = cv.FONT_HERSHEY_SIMPLEX

classification_model = Helper.loadModel('./model/traffic.h5') #load mask detection model
classes_classification = []
with open("./model/signs_classes.txt", "r") as f:
    classes_classification = [line.strip() for line in f.readlines()]

    for i in range(len(all_images)):
        img = all_images[i]
        #get image shape
        height, width, channels = img.shape

        # Detecting objects (YOLO)
        blob = cv.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Showing informations on the screen (YOLO)
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > confidence_threshold:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
                    
        indexes = cv.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        for j in range(len(boxes)):
            if j in indexes:
                x, y, w, h = boxes[j]
                label = str(classes[class_ids[j]]) + "=" + str(round(confidences[j]*100, 2)) + "%"
                img = cv.rectangle(img, (x, y), (x + w, y + h), (255,0,0), 2)
                crop_img = img[y:y+h, x:x+w]
                if len(crop_img) >0:
                    crop_img = cv.resize(crop_img, (WIDTH, HEIGHT))
                    crop_img =  crop_img.reshape(-1, WIDTH,HEIGHT,3)
                    prediction = np.argmax(classification_model.predict(crop_img))
                    print(prediction)
                    label = str(classes_classification[prediction])
                    img = cv.putText(img, label, (x, y), font, 0.5, (255,0,0), 2)

        cv.imwrite(str(output_folder_path)+'/'+ str(i+1) + '.jpg', img)
        print("finish image" + str(i+1))
