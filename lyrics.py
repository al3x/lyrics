from betterhandler import *
import cgi
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.webapp import template
from models import *
import os
import wsgiref.handlers

class MainPage(BetterHandler):
    def get(self):
        lyrics = db.GqlQuery("SELECT * FROM Lyric ORDER BY date DESC LIMIT 10")
        
        for_template = {
            'lyrics': lyrics,
        }
        
        self.response.out.write(template.render(self.template_path('index.html'), self.template_values(for_template)))
    
    
class NewLyric(BetterHandler):
    def get(self):
        self.response.out.write(template.render(self.template_path('new_lyric.html'), self.template_values()))
        
    def post(self):
        body = cgi.escape(self.request.get('body'))
        song = cgi.escape(self.request.get('song'))
        artist = cgi.escape(self.request.get('artist'))
        album = cgi.escape(self.request.get('album'))
        ASIN = cgi.escape(self.request.get('ASIN'))
        
        lyric = Lyric()
        lyric.user = users.get_current_user()
        lyric.body = unicode(body)
        lyric.song = unicode(song)
        lyric.artist = unicode(artist)
        lyric.album = unicode(album)
        lyric.ASIN = unicode(ASIN)

        lyric.put()
        
        for_template = {
            'lyric': lyric,
        }
        
        self.response.out.write(template.render(self.template_path('lyric.html'), self.template_values(for_template)))
        

class Artist(BetterHandler):
    def get(self):
        artist = cgi.escape(self.request.get('name'));
        
        lyrics = db.GqlQuery("SELECT * FROM Lyric WHERE artist = :1 ORDER BY date DESC", artist);
        
        if lyrics.count() < 1:
            lyrics = None;
        
        for_template = {
            'artist': artist,
            'lyrics': lyrics,
        }
        
        self.response.out.write(template.render(self.template_path('artist.html'), self.template_values(for_template)))


def main():
    application = webapp.WSGIApplication([
                                            ('/', MainPage),
                                            ('/lyric/new', NewLyric),
                                            ('/artist', Artist)
                                         ],
                                         debug=True)
                                       
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()