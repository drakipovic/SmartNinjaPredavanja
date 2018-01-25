#!/usr/bin/env python
import os
import jinja2
import webapp2


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


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")


class LoginHandler(BaseHandler):
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")

        return self.write("{} {}".format(username, password))


class CalculatorHandler(BaseHandler):
    def get(self):
        return self.render_template("calculator.html")

    def post(self):
        first_number = int(self.request.get("first_number"))
        second_number = int(self.request.get("second_number"))

        operation = self.request.get("operation")

        result = 0
        if operation == '+':
            result = first_number + second_number
        elif operation == '-':
            result = first_number - second_number
        elif operation == '*':
            result = first_number * second_number
        else:
            if second_number != 0:
                result = first_number / second_number

        params = {"first_number": first_number, "second_number": second_number,
                  "operation": operation, "result": result}

        return self.render_template("calculator.html", params=params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/login', LoginHandler),
    webapp2.Route('/calculator', CalculatorHandler)
], debug=True)
