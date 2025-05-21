"""
ASGI config for remind_me_later project.
"""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'remind_me_later.settings')
application = get_asgi_application()
