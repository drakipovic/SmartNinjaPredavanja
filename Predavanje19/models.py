from google.appengine.ext import ndb

class Message(ndb.Model):
    text = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.text, self.created)