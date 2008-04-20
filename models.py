from google.appengine.ext import db
from google.appengine.api import users

class Lyric(db.Model):
    body = db.TextProperty()
    artist = db.StringProperty()
    album = db.StringProperty()
    ASIN = db.StringProperty()
    song = db.StringProperty()
    user = db.UserProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    
class Favorite(db.Model):
    user = db.UserProperty(required=True)
    lyric = db.ReferenceProperty(Lyric)
    date = db.DateTimeProperty(auto_now_add=True)
    