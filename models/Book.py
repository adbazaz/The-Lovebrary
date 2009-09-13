from google.appengine.ext import db

class Book(db.Model):
    title = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)
