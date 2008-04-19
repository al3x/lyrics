from google.appengine.ext import db
from google.appengine.api import users

class Lyric(db.Model):
    body = db.TextProperty()
    owner = db.UserProperty(required=True)