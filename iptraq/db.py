from google.appengine.ext import db

class IPMark(db.Model):
    created = db.DateTimeProperty(auto_now_add=True)

class IPUpdate(db.Model):
    mark = db.ReferenceProperty(IPMark, collection_name="updates")
    created = db.DateTimeProperty(auto_now_add=True)
    ip_addr = db.StringProperty()

    @classmethod
    def from_request(cls, mark, request):
        return cls(mark=mark, ip_addr=request.remote_addr)
