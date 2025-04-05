"""
WSGI config for econtentproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

# Add both project root and project directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

for path in [project_root, project_dir]:
    if path not in sys.path:
        sys.path.append(path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'econtentproject.settings')

application = get_wsgi_application()
