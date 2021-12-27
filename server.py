import bottle
import json

import Application


@bottle.route("/")
def serve_html():
  return bottle.static_file("index.html",root="./html")

@bottle.route("/front_end.js")
def serve_front_end_js():
  return bottle.static_file("front_end.js",root="./html")

@bottle.route("/ajax.js")
def serve_AJAX():
  return bottle.static_file("ajax.js",root="html/")

@bottle.post("/mintemp")
def serve_mintemp():
  data = Application.mintemp_avg()
  json_export = json.dumps(data)
  return json_export


@bottle.post("/maxtemp")
def serve_maxtemp():
  data = Application.mintemp_avg()
  json_export = json.dumps(data)
  return json_export