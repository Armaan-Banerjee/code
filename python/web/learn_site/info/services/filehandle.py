import requests

class FileHandle:
    def __init__(self, baseurl, file):
        self.baseurl = baseurl
        self.file = file

    
    def upload(self):
        url = self.baseurl + "/upload"
        files = {"upload[]": ""}
        requests.post(self.file)
    