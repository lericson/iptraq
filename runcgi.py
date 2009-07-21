# Insert all .zip package stuffies.
import sys
from glob import glob
sys.path[:] = glob("*.zip") + sys.path
# Have to do this here so the next import of werkzeug actually does the
# import... Silly zipimporter.
import werkzeug

from iptraq.app import iptraq_app

if __name__ == "__main__":
    from wsgiref.handlers import CGIHandler
    CGIHandler().run(iptraq_app)
