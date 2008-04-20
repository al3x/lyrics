from google.appengine.ext import webapp
from google.appengine.api import users
import os

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