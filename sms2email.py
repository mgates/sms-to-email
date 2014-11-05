from flask import Flask
from flask import request
from flask.ext.basicauth import BasicAuth
import boto.ses
import os

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = os.environ['USER']
app.config['BASIC_AUTH_PASSWORD'] = os.environ['PASSWORD']

basic_auth = BasicAuth(app)

@app.route('/message')
@basic_auth.required
def message():
    subject = "Text Message from %s" % request.args.get('From')
    content = "Body: %(body)s \nMedia: %(url)s" % {"body": request.args.get('Body'), "url":request.args.get('MediaUrl0')}
    send_mail(subject, content)
    return("", 200)

def send_mail(subject, content):
    conn = boto.ses.connect_to_region(
            'us-east-1',
            aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
            aws_secret_access_key=os.environ['AWS_SECRET_KEY'])
    conn.send_email(
            'team@gopartage.com',
            subject,
            content,
            ['micahgates@gopartage.com'])

    return True


if __name__ == '__main__':
    app.run( debug=True )

