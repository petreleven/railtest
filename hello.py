from flask import Flask
import cv2

app = Flask(__name__)

@app.route("/")
def server():
    return "hello"


#app.run(debug=True, port="5000", host="0.0.0.0")