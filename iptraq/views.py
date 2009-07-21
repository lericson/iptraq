import datetime
from werkzeug import Response
from iptraq.db import IPMark, IPUpdate
from iptraq.utils import key_response

history_limit = datetime.timedelta(days=1)

def create_mark(request):
    mark = IPMark()
    mark.put()
    update = IPUpdate.from_request(mark, request)
    update.put()
    return key_response(mark, update)

def list_mark(request, key):
    mark = IPMark.get(key)
    update_texts = []
    updates = mark.updates.order("-created")
    updates.filter("created >", datetime.datetime.now() - history_limit)
    for update in updates.fetch(100):
        text = "%s: %s\n" % (update.created.isoformat(), update.ip_addr)
        update_texts.append(text)
    return Response("".join(update_texts), mimetype="text/plain")

def update_mark(request, key):
    if request.method != "POST":
        raise MethodNotAllowed(["POST"])
    mark = IPMark.get(key)
    update = IPUpdate.from_request(mark, request)
    update.put()
    return key_response(mark, update)
