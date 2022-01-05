import numpy as np
import tensorflow as tf
from tensorflow import keras
import pickle as pkl


modelFile='./model/traffic.h5'
testing_file = "./test/test.p"

with open(testing_file, mode='rb') as f:
    test = pkl.load(f)
X_test = test['features']
y_test = test['labels']
X_test = np.array(X_test)
y_test = np.array(y_test)
model = keras.models.load_model(modelFile)

results = model.evaluate(X_test, y_test)
print(results)


index = 0
img_testing = X_test[index]
label_testing = y_test[index]

actual = np.argmax(label_testing)

prediction = np.argmax(model.predict(img_testing))
print(prediction)

