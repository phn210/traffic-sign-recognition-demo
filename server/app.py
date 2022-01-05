from flask import Flask, request, url_for, redirect, render_template, jsonify
# import numpy as np
# import tensorflow as tf
# from tensorflow import keras
# import pickle as pkl


# modelFile='traffic.h5'
# testing_file = "test.p"

# with open(testing_file, mode='rb') as f:
#     test = pkl.load(f)
# X_test = test['features']
# y_test = test['labels']
# X_test = np.array(X_test)
# y_test = np.array(y_test)
# model = keras.models.load_model(modelFile)

app = Flask(__name__)

@app.route('/')
def home():
    return {"notice": "welcome!!!"}

@app.route('/api', methods=['GET'])
def testAPI():
    return {"test" : "okay"}

# @app.route('/evaluate')
# def evaluate():
#     results = model.evaluate(X_test, y_test)
#     return {
#             'results_evaluate': results,
#             }

# @app.route('/predict',methods=['POST'])
# def predict():
#     data = request.get_json()
#     print(data)
#     print(data['index'])
#     index = data['index']
#     img_testing = X_test[index]
#     label_testing = y_test[index]

#     actual = np.argmax(label_testing)

#     prediction = np.argmax(model.predict(img_testing))
#     return {
#             'actual':actual,
#             'prediction':prediction,
#             }


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
