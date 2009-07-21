from werkzeug import Response

def key_response(*models):
    data = "".join("%s: %s\n" % (mdl.kind(), mdl.key()) for mdl in models)
    return Response(data, mimetype="text/plain")
