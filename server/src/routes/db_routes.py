from flask_restx import Resource

from src import db
from src.lib.WHE_scrape import whe_scrape

@db.route('/update_db')
class UpdateDB(Resource):
    def get(self):
        return {'update_db': whe_scrape.update_db()}