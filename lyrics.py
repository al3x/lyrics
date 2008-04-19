from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.webapp import template
import models
import os
import wsgiref.handlers

class BetterHandler(webapp.RequestHandler):
    def template_path(self, filename):
        return os.path.join(os.path.dirname(__file__), 'templates', filename)

    def template_values(self, extra_dict=None):
        standard_values = { 
            'user': users.get_current_user(),
            'login_url': users.create_login_url('/'),
            'logout_url': users.create_logout_url('/'),
        }

        if extra_dict:
            standard_values.update(extra_dict)

        return standard_values


class MainPage(BetterHandler):
    def get(self):
        self.response.out.write(template.render(self.template_path('index.html'), self.template_values()))
    
    
class NewLyric(BetterHandler):
    def get(self):
        self.response.out.write(template.render(self.template_path('new_lyric.html'), self.template_values()))
        
        
def main():
  application = webapp.WSGIApplication([('/', MainPage),
                                        ('/lyric/new', NewLyric)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
  main()