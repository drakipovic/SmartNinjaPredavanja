#!/usr/bin/env python
import os
import jinja2
import webapp2
from model import Message
from google.appengine.api import users


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

        user = users.get_current_user()
        if user:
            params["loggedIn"] = True
            params["logOutUrl"] = users.create_logout_url('/')
        else:
            params["loggedIn"] = False
            params["logInUrl"] = users.create_login_url('/')

        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            archived = self.request.get("archived")
            if archived == "":
                archived = False
            else:
                archived = True

            sent = self.request.get("sent")
            if sent == "":
                sent = False
            else:
                sent = True

            return self.render_template("home.html", params={
                "messages": Message.query(
                    Message.archived == archived and (
                        (sent and Message.from_email == user.email())
                        or
                        (not sent and Message.to_email == user.email())
                    )
                ).fetch(),
                "archived": archived,
                "sent": sent,
                "logoutUrl": users.create_logout_url("/")
            })
        else:
            return self.render_template("login.html", params={
              "loginUrl": users.create_login_url("/")
            })

    def post(self):
        user = users.get_current_user()
        if user:
            message = Message.get_by_id(int(self.request.get("id")))
            message.archived = not message.archived
            message.put()
            return self.redirect_to("home")
        else:
            return self.render_template("login.html", params={
              "loginUrl": users.create_login_url("/")
            })

class NewHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            return self.render_template("new.html")
        else:
            return self.render_template("login.html", params={
              "loginUrl": users.create_login_url("/")
            })
    def post(self):
        user = users.get_current_user()
        if user:
            to_email = self.request.get("to")
            subject = self.request.get("subject")
            content = self.request.get("content")
            message = Message(from_email = user.email(), to_email=to_email, subject=subject, content=content)
            message.put()
            return self.redirect_to("home")
        else:
            return self.render_template("login.html", params={
              "loginUrl": users.create_login_url("/")
            })


class DeleteHandler(BaseHandler):
    def get(self, message_id):
        user = users.get_current_user()
        if user:
            return self.render_template("delete.html", params={
                "message": Message.get_by_id(int(message_id))
            })
        else:
            return self.render_template("login.html", params={
              "loginUrl": users.create_login_url("/")
            })
    def post(self, message_id):
        user = users.get_current_user()
        if user:
            message = Message.get_by_id(int(message_id))
            message.key.delete()
            return self.redirect_to("home")
        else:
            return self.render_template("login.html", params={
              "loginUrl": users.create_login_url("/")
            })
class ViewHandler(BaseHandler):
    def get(self, message_id):
        user = users.get_current_user()
        if user:
            return self.render_template("view.html", params={
                "message": Message.get_by_id(int(message_id))
            })
        else:
            return self.render_template("login.html", params={
              "loginUrl": users.create_login_url("/")
            })

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="home"),
    webapp2.Route('/new', NewHandler),
    webapp2.Route('/message/<message_id:\d+>', ViewHandler),
    webapp2.Route('/message/<message_id:\d+>/delete', DeleteHandler),
], debug=True)
