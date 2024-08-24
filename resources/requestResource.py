from flask_restful import Resource
from flask import request
import json
from util import zoom

class RequestPOSTResource(Resource):
    def post(self):
        if request.data:
            data = json.loads(request.data)
            return zoom.PostAlertZoom(data)
        else :
            no_data = 'No JSON data'
            return no_data
