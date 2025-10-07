from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/hello', methods=['GET'])
    def hello():
        return 'Hello, World! Smart Data Pipeline is alive.'

    return app
