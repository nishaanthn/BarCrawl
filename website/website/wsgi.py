import os
import sys

sys.path.append('/home/dougiefresh49/BarCrawl/website/website_files')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website_files.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
