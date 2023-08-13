from flask import Flask, Blueprint
from .extensions import api

from .routes.search_routes import Search, Metadata

api_bp = Blueprint('api', __name__, url_prefix='/api')

def create_app():
    app = Flask(__name__, static_url_path='/', static_folder='../../client/dist')

    @app.route('/', defaults={'path': ''})
    @app.route('/<string:path>')
    def serve_static(path):
      try:
          return app.send_static_file(path)
      except:
          return app.send_static_file('index.html')

    api.init_app(api_bp)

    app.register_blueprint(api_bp)

    api.add_resource(Search, '/search/<keyword>')
    api.add_resource(Metadata, '/metadata')  

    return app