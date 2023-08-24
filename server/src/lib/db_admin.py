from db_connection import db_connection

def update_db():
  db_connection.add_decisions()

update_db()