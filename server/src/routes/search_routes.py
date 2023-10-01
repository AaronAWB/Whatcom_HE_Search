from datetime import datetime
from flask import request
from flask_restx import Resource
from sqlalchemy import and_

from src import api
from server.src.lib.data_extraction import extract_data
from src.models.decisions import Decision

@api.route('/search')
class Search(Resource):
    def get(self):
        keyword = request.args.get('keyword')
        examiner = request.args.get('examiner')
        hearing_date = request.args.get('hearingDate')
        decision_date = request.args.get('decisionDate')
        decision_month = request.args.get('month')
        decision_year = request.args.get('year')


        filters = []
        if keyword:
          filters.append(Decision.text.ilike(f'%{keyword}%'))
        if examiner:
          filters.append(Decision.hearing_examiner.ilike(f'%{examiner}%'))
        if hearing_date:
          hearing_date = datetime.strptime(hearing_date, '%Y-%m-%d').strftime('%B %d, %Y')
          filters.append(Decision.hearing_date.ilike(f'%{hearing_date}%'))
        if decision_date:
          decision_date = datetime.strptime(decision_date, '%Y-%m-%d').strftime('%B %d, %Y')
          filters.append(Decision.decision_date.ilike(f'%{decision_date}%'))
        if decision_month:
          filters.append(Decision.decision_date.ilike(f'%{decision_month}%'))
        if decision_year:
          filters.append(Decision.decision_date.ilike(f'%{decision_year}%'))
        
        search_results = Decision.query.filter(and_(*filters))
        

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
    return {'metadata': extract_data.get_metadata()}

