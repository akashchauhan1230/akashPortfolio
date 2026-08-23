"""
WSGI config for AkashPortfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

# pyrefly: ignore [missing-import]
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AkashPortfolio.settings')

application = get_wsgi_application()
app = application
