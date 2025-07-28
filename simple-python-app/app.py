from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, new version v2 released!'

if __name__ == '__main__':
    app.run()

