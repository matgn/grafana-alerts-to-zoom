import os
import json


class ENVIRONMENT:
    def __init__(self):
        self.zoom_endpoint = os.getenv("ZOOMENDPOINT")
        self.zoom_token = os.getenv("ZOOMTOKEN")
        self.prefix = os.getenv("PREFIX")

    def get_instance(self):
        if not hasattr(self, "_instance"):
            self._instance = ENVIRONMENT()
        return self._instance

    def getZoomEndpoint(self):
        return self.zoom_endpoint

    def getZoomToken(self):
        return self.zoom_token
    
    def getPrefix(self):
        return self.prefix
    
zoom_endpoint = ENVIRONMENT().get_instance().getZoomEndpoint()
zoom_token = ENVIRONMENT().get_instance().getZoomToken()
prefix = ENVIRONMENT().get_instance().getPrefix()