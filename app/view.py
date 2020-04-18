
from flask import Flask, render_template

from app import picdownload
import base64
DATABASE = '/tmp/flaskr.db'
ENV = 'development'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['GET'])
def mainpage():
    return render_template('index.html')

## todo method not allow error 
@app.route('/download', methods=['GET', 'POST'])
def download(encodeurl):
    print("download in")
    print(encodeurl)
    url = base64.b64decode(encodeurl)
    picdownload.download(url, "./")

    return "success"

if __name__ == '__main__':
    app.run()
