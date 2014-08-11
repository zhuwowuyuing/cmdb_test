"""
WSGI config for cmdb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys

# import site

# ve_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib/python2.7/site-packages"))
# # Add the virtual Python environment site-packages directory to the path
# site.addsitedir(ve_path)


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cmdb.settings")

# # Activate your virtual env
# activate_env=os.path.expanduser("/data/webroot/env_python2.7/bin/activate_this.py")
# execfile(activate_env, dict(__file__=activate_env))


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()