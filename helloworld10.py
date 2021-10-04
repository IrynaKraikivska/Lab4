from flask import Flask
#from flask import request, jsonify
from waitress import serve

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Hello World!"

    @app.route('/api/v1/hello-world-10')
    def api_all():
        return "Hello World 10"

    return app

app = create_app()
serve(app, host ='127.0.0.1', port=5000)