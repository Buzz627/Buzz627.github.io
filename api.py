from flask import Flask

app = Flask(__name__)

@app.route('/api/all')
def hello():
    return 'Hello, World!'