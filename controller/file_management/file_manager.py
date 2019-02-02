from config import Config
from controller.file_management.simple_file_storage import SimpleFileStorage
from controller.dbHandler.db_handler import DbHandler
import random

db_handler = DbHandler()

class FileManager():
    def check_file(self,file_id,user_id):
        if file_id:
            return db_handler.get_file_info_from_db(file_id)

    def generate_pulic_url(self,file_id):
        pass

    def generate_private_url(self,file_id,user_id):
        self.access_file_to_user(file_id,user_id)
        file = db_handler.get_file_info_from_db(file_id)
        return self.translate_file_address(Config+user_id+"/"+file.file_id+"."+file.file_type)

    def download_file(self,url):
        file_storage = SimpleFileStorage()
        return file_storage.download_file(url)

    def translate_file_address(self,url):
        return url

    def access_file_to_user(self,file_id,user_id):
        #todo move file
        pass




