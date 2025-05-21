"""
WSGI config for remind_me_later project.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'remind_me_later.settings')
application = get_wsgi_application()
