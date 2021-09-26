"""
WSGI config for time_table project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/dongryun/garrage_box/app'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'time_table.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
