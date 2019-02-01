from flask import Flask, url_for, send_file, request

from controller.file_management.file_manager import FileManager

app = Flask(__name__)
file_manager = FileManager()
@app.route('/')
def api_root():
    return 'welcome to spotify'

@app.route('/getfile')
def get_file():
    user_id = request.args.get('user_id')
    file_id = request.args.get('file_id')

    return file_manager.check_file(file_id,user_id)

@app.route('/download')
def download_file():
    file_id = request.args.get('url')
    print(file_manager.download_file(file_id))
    return send_file(file_manager.download_file(file_id),'audio/mp3')


if __name__ == '__main__':
    app.run()