import os
from flask import request, make_response, jsonify
from flask_restful import Resource
from werkzeug.utils import secure_filename
from . import RESOURCE_NOT_FOUND, RESOURCE_OK, error_resp, success_resp
from service import logger
from service.FileService import FileService
import pandas as pd

ALLOWED_EXTENSIONS = set(['csv'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class UploadResource(Resource):
    def post(self):
        try:
            if request.method == 'POST':
                if 'file' not in request.files:
                    return error_resp('File not found.'), RESOURCE_NOT_FOUND
                file = request.files['file']
                if file.filename == '':
                    return error_resp('Invalid file name.'), RESOURCE_NOT_FOUND
                if file and allowed_file(file.filename):
                    FileService.upload(file)
                    return success_resp("Success"), RESOURCE_OK
                else:
                    return error_resp('Invalid file type.'), RESOURCE_NOT_FOUND
        except ValueError as e:
            return error_resp(str(e)), RESOURCE_NOT_FOUND
