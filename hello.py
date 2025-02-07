from flask import Flask, redirect, request

app = Flask(__name__)

@app.before_request
def before_request():
    if not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)


#app.run(debug=True, port="5000", host="0.0.0.0")
