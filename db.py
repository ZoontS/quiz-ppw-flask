import click
import pymongo
from flask import current_app, g
from flask.cli import with_appcontext

def init_db_command():
  init_db()
  click.echo('Initialized the database')
  
def init_app():
  app.teardown_appcontext(close_db)
  app.cli.add_command(init_db_command)
