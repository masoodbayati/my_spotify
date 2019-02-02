from flask import Flask, url_for, send_file, request

from controller.file_management.file_manager import FileManager
from controller.search_management.search_management import SearchManagement

app = Flask(__name__)
file_manager = FileManager()
seach_management = SearchManagement()
@app.route('/')
def api_root():
    return 'welcome to spotify'

@app.route('/getfile')
def get_file():
    user_id = request.args.get('user_id')
    file_id = request.args.get('file_id')

    return file_manager.check_file(file_id,user_id).get_json_str()

@app.route('/download')
def download_file():
    file_id = request.args.get('url')
    return send_file(file_manager.download_file(file_id),'audio/mp3')

@app.route('/search')
def search():
    query = request.args.get('query')
    search_types = request.args.get('types')
    return seach_management.get_json_string( seach_management.search(query,search_types))

if __name__ == '__main__':
    app.run()