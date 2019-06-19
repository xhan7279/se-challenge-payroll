import os
from flask import request, make_response, jsonify
from flask_restful import Resource
from . import RESOURCE_NOT_FOUND, RESOURCE_OK, error_resp, success_resp
from service.ReportService import RepportService


class ReportResource(Resource):
    @staticmethod
    def get():
        try:
            if request.method == 'GET':
                data = RepportService.generate_report()
                return success_resp(str(data)), RESOURCE_OK
        except ValueError as e:
            return error_resp(str(e)), RESOURCE_NOT_FOUND
