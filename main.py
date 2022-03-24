import flask 
from pyresparser import ResumeParser
from flask import request, jsonify, url_for
from flask_cors import cross_origin
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = '../'
app = flask.Flask(__name__) 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route('/parser', methods = ['POST'])
@cross_origin()
def process():
    file = request.files['file']
    filename = secure_filename(file.filename)
    filePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filePath)
    result = ResumeParser(filePath).get_extracted_data()
    print('result:', result)
    return result

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__': 
    app.run(host='0.0.0.0') 