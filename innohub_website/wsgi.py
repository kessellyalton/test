"""
WSGI config for innohub_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from decouple import config

# Load the settings module from environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'innohub_website.settings')

# Check if running on Railway and set the correct settings
if config('RAILWAY_ENVIRONMENT', default=None):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'innohub_website.settings'

application = get_wsgi_application()
