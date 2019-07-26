from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/what_next', methods = ['POST'])
def what_next():
   incoming_data= request.get_json()
   return('OK')

@app.route('/insertbuild' , methods=['POST'])
def insertbuild():
    incoming_data = request.get_json()
    return("OK")

if __name__ == '__main__':
    app.run()