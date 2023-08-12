from flask_restx import Resource

from src import api
from src.lib.WHE_scrape import whe_scrape

@api.route('/search/<keyword>')
class Search(Resource):
  def get(self, keyword):
    return {'search_results': whe_scrape.search_keyword(keyword)}

@api.route('/metadata/<pdf>')
class Metadata(Resource):
  def get(self, pdf):
    return {'metadata': whe_scrape.get_metadata(pdf)}