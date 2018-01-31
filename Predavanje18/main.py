#!/usr/bin/env python
import os
import jinja2
import webapp2

from random import randint

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


class City(object):

    def __init__(self, name, country_name, city_image_url):
        self.name = name
        self.country_name = country_name
        self.city_image_url = city_image_url

cities = [City("London", "Great Britain", "/assets/img/london.jpeg"),
          City("Dublin", "Ireland", "/assets/img/dublin.jpeg"),
          City("Zagreb", "Croatia", "/assets/img/zagreb.jpeg"),
          City("Paris", "France", "/assets/img/paris.jpeg"),
          City("Amsterdam", "Netherlands", "/assets/img/amsterdam.jpg")]


class QuizHandler(BaseHandler):
    def get(self):
        city_index = randint(0, 5)

        city = cities[city_index]

        params = {"country_name": city.country_name, "image_url": city.city_image_url}
        return self.render_template("quiz.html", params=params)

    def post(self):
        country_name = self.request.get("country_name")
        city_name = self.request.get("capital")

        result = False
        for city in cities:
            if city.country_name == country_name and city.name == city_name:
                result = True


        if result:
            feedback = "Correct"
        else:
            feedback = "Not correct"

        params = {"result": feedback, "country_name": country_name,
                  "capital": city_name}
        return self.render_template("quiz.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/quiz', QuizHandler)
], debug=True)
