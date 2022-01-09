from flask import Flask, request, url_for, redirect, render_template, jsonify
app = Flask(__name__)


@app.route('/')
def home():
    return {"notice": "welcome!!!"}


@app.route('/api', methods=['GET'])
def testAPI():
    return {"test" : "okay"}


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
