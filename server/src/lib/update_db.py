from . import db_connection

def add_decisions():
  db_connection.add_decisions()
  print('Database updated.')

add_decisions()