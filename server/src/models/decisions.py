from src import db

class Decision(db.Model):
  __tablename__ = 'decisions'
  id = db.Column(db.Integer, primary_key = True)
  case_name = db.Column(db.String(100), nullable = False)
  hearing_examiner = db.Column(db.String(50), nullable = False)
  hearing_date = db.Column(db.String(20), nullable = False)
  decision_date = db.Column(db.String(20), nullable = False)
  text = db.Column(db.Text, nullable = False)
  link = db.Column(db.String(100), nullable = False)







  