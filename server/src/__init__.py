import os

from flask import Flask, Blueprint
from .extensions import api, db

from dotenv import load_dotenv; load_dotenv()

from .routes.search_routes import Search, Metadata
from .routes.db_admin_routes import UpdateDB

api_bp = Blueprint('api', __name__, url_prefix='/api')

def create_app():
    app = Flask(__name__, static_url_path='/', static_folder='../../client/dist')

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_CONNECTION_STRING')

    @app.route('/', defaults={'path': ''})
    @app.route('/<string:path>')
    def serve_static(path):
      try:
          return app.send_static_file(path)
      except:
          return app.send_static_file('index.html')

    api.init_app(api_bp)
    db.init_app(app)

    app.register_blueprint(api_bp)
    
    api.add_resource(Search, '/search/<keyword>')
    api.add_resource(Metadata, '/metadata')
    api.add_resource(UpdateDB, '/update_db')

    return app