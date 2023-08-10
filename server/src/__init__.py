from flask import Flask, Blueprint

api_bp = Blueprint('api', __name__, url_prefix='/api')

def create_app():
    app = Flask(__name__)

    app.register_blueprint(api_bp)

    return app