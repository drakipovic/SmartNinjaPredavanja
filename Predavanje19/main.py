import os

import jinja2
import webapp2

from models import Message


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")


class ResultHandler(BaseHandler):
    def post(self):
        result = self.request.get("some_text")

        message = Message(text=result)
        message.put()

        return self.write(result)


class MessageListHandler(BaseHandler):
    def get(self):
        messages = Message.query().fetch()

        params = {"messages": messages}

        return self.render_template("message_list.html", params=params)


class MessageDetailsHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))

        params = {"message": message}

        return self.render_template("message_details.html", params=params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/result', ResultHandler),
    webapp2.Route('/message-list', MessageListHandler),
    webapp2.Route('/message/<message_id:\d+>', MessageDetailsHandler)
], debug=True)