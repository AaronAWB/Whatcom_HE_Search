from flask_restx import Resource

from src import api
from src.lib.db_connection import db_connection
from src.lib.WHE_scrape import whe_scrape

@api.route('/update_db')
class UpdateDB(Resource):
  def post(self):
    db_connection.add_decisions()
    return 'Database updated.', 201
  
@api.route('/extract_text/<link>')
class ExtractTextFromImage(Resource):
  def post(sel, link):
    extracted_text = whe_scrape.extract_text_from_img(link)
    return extracted_text, 200
