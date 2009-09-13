import os

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

from models.Book import *

class MainPage(webapp.RequestHandler):
    def get(self):

        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
            name = user.nickname()
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            name = "Anonymous"

        B = Book.gql("ORDER BY date DESC LIMIT 10")
        if B and B.count() == 0:
            newB = Book()
            newB.title = "Lovie Book"
            newB.put()
            newB2 = Book()
            newB2.title = "Lovie Book #2"
            newB2.put()

        book_list = []
        B = Book.gql("ORDER BY date DESC LIMIT 10")
        if B and B.count() != 0:
            for book in B:
                book_list.append(book)

        template_values = {
          'url': url,
          'url_linktext': url_linktext,
          'name': name,
          'book_list': book_list
          }

        path = os.path.join('templates', 'index.html')
        self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
