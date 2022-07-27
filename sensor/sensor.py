import os
import sqlite3
import threading
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
from .readings import get_readings

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'sensor.db'),
    SECRET_KEY='dev'
))

app.config.from_envvar('SENSOR_SETTINGS', silent=True)

def init_db():
    db = get_db()

    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    print('Initialized the database.')

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def index():
    return render_template('index.html', data=get_readings())


from . import background
sensor_daemon = threading.Thread(target=background.scheduler, name='Background')
sensor_daemon.start()
