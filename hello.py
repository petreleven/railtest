from flask import Flask


app = Flask(__name__)

@app.route("/")
def server():
    return "hello"


app.run(debug=True, port="5000")