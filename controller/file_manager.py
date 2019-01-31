from controller.simple_file_storage import SimpleFileStorage


class FileManager():
    def check_file(self,file_id):
        pass

    def generate_pulic_url(self,file_id):
        pass

    def generate_private_url(self,file_id,user_id):
        pass

    def download_file(self,url):
        file_storage = SimpleFileStorage()
        file_storage.get_file(url)





