from flask import Flask
from flask.ext.basicauth import BasicAuth
import os

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = os.environ['USER']
app.config['BASIC_AUTH_PASSWORD'] = os.environ['PASSWORD']
basic_auth = BasicAuth(app)


@app.route('/message', methods=["POST"])
@basic_auth.required
def message(self):
    self.send_message(content)
    return("", 200)

def send_message(self, content):
    "asdf"
    
if __name__ == '__main__':
    app.run()

