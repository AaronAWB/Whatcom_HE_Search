from flask import request
from flask_restx import Resource

from src import api
from src.lib import whe_scrape

@api.route('/search/<keyword>')
class Search(Resource):
    def get(self, keyword):
        return {'search_results': whe_scrape.search_keyword(keyword)}