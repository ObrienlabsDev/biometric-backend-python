# 20240811 https://github.com/ObrienlabsDev/biometric-backend-python

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/health')
def hello():
    return '{ "health" : true }'

if __name__ == "__main__":
    app.run(debug=True)
