from google.appengine.ext import ndb


class GuestbookMessage(ndb.Model):

    name = ndb.StringProperty()
    email = ndb.StringProperty()

    text = ndb.TextProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)