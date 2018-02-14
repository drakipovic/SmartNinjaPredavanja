#!/usr/bin/env python
import os
import json

import jinja2
import webapp2
from google.appengine.api import urlfetch



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
        data = open('people.json', 'r').read()
        people = json.loads(data)

        params = {"people_list": people}
        return self.render_template("hello.html", params=params)


class WeatherHandler(BaseHandler):
    def get(self):
        city = self.request.get('city')

        if city:
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=7cdda3b361013de4921ef9ee13b83644".format(city)

            res = urlfetch.fetch(url)
            weather_info = json.loads(res.content)
            params = {"weather_info": weather_info}

        else:
            params = {}

        return self.render_template('weather.html', params=params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/weather', WeatherHandler)
], debug=True)
