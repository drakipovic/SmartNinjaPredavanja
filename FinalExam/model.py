from google.appengine.ext import ndb

class Message(ndb.Model):
    from_email = ndb.StringProperty()
    to_email = ndb.StringProperty()
    subject = ndb.StringProperty()
    content = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    archived = ndb.BooleanProperty(default=False)