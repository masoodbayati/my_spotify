from models.jsonable import Jsonable


class Client(Jsonable):
    def __init__(self,token,client_type,status):
        self.token = token
        self.client_type = client_type
        self.status = status

