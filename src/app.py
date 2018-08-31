from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hi!"

@app.route("/test")
def test():
    return "Hi Test!"

if __name__ == '__main__':
    app.run(port=3838)

