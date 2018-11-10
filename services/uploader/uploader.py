import os
from flask import Flask, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('Uploader Service')

UPLOAD_FOLDER = '../../uploads'
ALLOWED_EXTENTIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
CORS(app, expose_headers='Authorization')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.before_request
def log_request_info():
    logger.debug('Headers: %s', request.headers)
    logger.debug('Body: %s', request.get_data())

@app.route('/upload', methods=['POST'])
def uploadFile():
    target = os.path.join(UPLOAD_FOLDER)
    if not os.path.isdir(target):
        os.mkdir(target)
    
    file = request.files['file']
    filename = secure_filename(file.filename)
    destination="/".join([target, filename])
    logger.info("uploaded file name: %s ", file.filename)
    file.save(destination)
    session['uploadFilePath']=destination
    response = "response - dont know what to return yet"

    return response



app.secret_key = os.urandom(24)
app.run(debug=True,host="0.0.0.0",use_reloader=False)
