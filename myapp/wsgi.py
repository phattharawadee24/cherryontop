import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
os.environ.setdefault('DJANGO_ALLOWED_HOSTS', '.vercel.app')

application = get_wsgi_application()