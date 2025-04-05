"""
WSGI config for econtentproject project.
"""

import os
import sys

# Calculate absolute path to project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

# Add to Python path
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'econtentproject.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
