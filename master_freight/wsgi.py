"""
WSGI config for master_freight project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os

# site.addsitedir('/home/master_freight/webapps/master_freight/lib/python2.7/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "master_freight.settings")

# activate_this = os.path.expanduser("~/webapps/master_freight/bin/activate_this.py")
# execfile(activate_this, dict(__file__=activate_this))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
