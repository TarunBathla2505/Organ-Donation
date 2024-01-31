from flask import Flask
from flask_session import Session
from flask_cors import CORS


app = Flask(__name__)
app.secret_key = 'ckjwbdfcjsbadfkcbkawbdsfjcbwaejkb'
app.config['SESSION_PERMANENT'] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
CORS(app,supports_credentials=True)

@app.route('/')
def hello():
    return 'Hello tarun bathla'

if __name__ == '__main__':
    app.run(debug=True)


from contoller import *


