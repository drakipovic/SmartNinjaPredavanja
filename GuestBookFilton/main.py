import os
import jinja2
import webapp2

from models import GuestbookMessage


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class GuestBookMessageHandler(BaseHandler):

    def get(self):
        return self.render_template("guestbook_message.html")

    def post(self):
        name = self.request.get("name")
        email = self.request.get("email")
        text = self.request.get("text")

        msg = GuestbookMessage(name=name, email=email, text=text)
        msg.put()

        return self.redirect_to("thanks-page")


class GuestBookMessageListHandler(BaseHandler):

    def get(self):
        messages = GuestbookMessage.query().fetch()
        params = {"messages": messages}

        return self.render_template("guestbook_message_list.html", params=params)


class GuestBookMessageDetailsHandler(BaseHandler):

    def get(self, message_id):
        message = GuestbookMessage.get_by_id(int(message_id))

        params={"message": message}
        return self.render_template("guestbook_message_details.html", params=params)


class GuestBookMessageEditHanlder(BaseHandler):

    def get(self, message_id):
        message = GuestbookMessage.get_by_id(int(message_id))

        params={"message": message}

        return self.render_template("guestbook_message_edit.html", params=params)

    def post(self, message_id):
        text = self.request.get("text")

        message = GuestbookMessage.get_by_id(int(message_id))
        message.text = text
        message.put()

        return self.redirect_to("msg-list")


class ThanksHandler(BaseHandler):

    def get(self):
        return self.write("Thanks for your message!")


app = webapp2.WSGIApplication([
    webapp2.Route('/', GuestBookMessageHandler),
    webapp2.Route('/thanks', ThanksHandler, name="thanks-page"),
    webapp2.Route('/messages', GuestBookMessageListHandler, name="msg-list"),
    webapp2.Route('/messages/<message_id:\d+>', GuestBookMessageDetailsHandler),
    webapp2.Route('/messages/<message_id:\d+>/edit', GuestBookMessageEditHanlder)
])