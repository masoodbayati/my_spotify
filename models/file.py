from models.jsonable import Jsonable
import json as json_handler


class File(Jsonable):
    def __init__(self,file_id,file_path,size,file_type,url):
        self.file_id = file_id
        self.file_path = file_path
        self.size = size
        self.file_type = file_type
        self.url = url

    def get_json_object(self):
        data = {
            "type": self.file_type,
            "file_id" :self.file_id,
            "size":self.size,
            "file_path": self.file_path,
            "url":self.url
        }
        return data

    def get_json_str(self):
        return json_handler.dumps(self.get_json_object())


        