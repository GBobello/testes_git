from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! This is a test of merge in git and snv. One more test."

if __name__ == "__main__":
    app.run()