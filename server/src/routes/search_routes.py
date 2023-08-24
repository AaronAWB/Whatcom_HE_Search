from flask_restx import Resource

from src import api
from src.lib.WHE_scrape import whe_scrape
from src.models.decisions import Decision

@api.route('/search/<keyword>')
class Search(Resource):
    def get(self, keyword):
        search_results = Decision.query.filter(or_(Decision.text.ilike(f'%{keyword}%')))
        result_list = [{
            'id': decision.id,
            'case_name': decision.case_name,
            'hearing_examiner': decision.hearing_examiner,
            'hearing_date': decision.hearing_date,
            'decision_date': decision.decision_date,
            'text': decision.text,
            'link': decision.link
        } for decision in search_results]

        return {'search_results': result_list}

@api.route('/metadata')
class Metadata(Resource):
  def get(self):
    return {'metadata': whe_scrape.get_metadata()}

