#!/usr/bin/env python

from werkzeug import Request
from werkzeug.exceptions import HTTPException
from werkzeug.routing import Map, Rule

from iptraq.views import create_mark, list_mark, update_mark

url_map = Map([
    Rule("/", methods=("POST",), endpoint=create_mark),
    Rule("/<key>/", methods=("GET",), endpoint=list_mark),
    Rule("/<key>/", methods=("POST",), endpoint=update_mark),
])

def iptraq_app(environ, start_response):
    urls = url_map.bind_to_environ(environ)
    try:
        endpoint, kwds = urls.match()
    except HTTPException, e:
        response = e
    else:
        request = Request(environ)
        response = endpoint(request, **kwds)
    return response(environ, start_response)
