import os, dj_database_url
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ['DJ_SECRET']
DEBUG      = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['*']          # Vercel sets Host header

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'rest_framework',
    'products', 'orders',
]

DATABASES = {
    'default': dj_database_url.parse(os.environ['DATABASE_URL'])
}

STATIC_URL  = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'