from config import Config
from controller.file_management.file_storage import FileStorage
from controller.dbHandler.db_handler import DbHandler

class SimpleFileStorage(FileStorage):
    def download_file(self,url):
        db_handler = DbHandler()
        return db_handler.get_file_binary_from_db(url)




