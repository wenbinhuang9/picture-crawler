import sys
from flask import Flask, helpers
from PicD

DATABASE = '/tmp/flaskr.db'
ENV = 'development'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

print("__name__ is")
print(__name__)
print(type(__name__))
print(helpers.get_root_path(__name__))
print(sys.modules.get(__name__))

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def download():
    pass

if __name__ == '__main__':
    app.run()
