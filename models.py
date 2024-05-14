"""
This file defines the database models
"""

import datetime
from .common import db, Field, auth
from pydal.validators import *


def get_user_email():
    return auth.current_user.get('email') if auth.current_user else None

def get_time():
    return datetime.datetime.utcnow()

db.define_table(
    'bird',
    Field('species', 'string', requires=IS_NOT_EMPTY()),
    Field('number_of_birds', 'integer', requires=IS_NOT_EMPTY()),
    Field('location', 'string', requires=IS_NOT_EMPTY()),
    Field('date', 'datetime', default=get_time),
)

if not db(db.bird).count():
    db.bird.insert(species='Pigeon', number_of_birds=10, location='New York')

db.commit()
