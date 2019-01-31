from models.jsonable import Jsonable


class File(Jsonable):
    def __init__(self,file_id,file_path,size,file_type,url):
        self.file_id = file_id
        self.file_path = file_path
        self.size = size
        self.file_type = file_type
        self.url = url

        