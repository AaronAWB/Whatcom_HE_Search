from src.lib.data_extraction import extract_data
from ..extensions import db
from src.models.decisions import Decision

class DB_Connection:

  def add_decisions(self):
      print('Adding decisions to database...')
      decisions = extract_data.retrieve_pdf_data()
      
      try:
      
        inspector = db.inspect(db.engine)
        tables = inspector.get_table_names()

        if 'decisions' not in tables:
          Decision.__table__.create(db.engine)

        for decision in decisions:
          if not self.decision_in_db(decision):
            new_decision = Decision(
                case_name = decision['case_name'],
                hearing_examiner = decision['hearing_examiner'],
                hearing_date = decision['hearing_date'],
                decision_date = decision['decision_date'],
                text = decision['pdf_text'],
                link = decision['link']
            )
            db.session.add(new_decision)
            db.session.commit()
            print(f'Decision {new_decision.case_name} added to database')
    
      except Exception as e:
        print(e)
        db.session.rollback()
        raise e

  def decision_in_db(self, decision):
    decision_in_db = Decision.query.filter_by(link = decision['link']).first()
    return decision_in_db is not None
  
db_connection = DB_Connection()
