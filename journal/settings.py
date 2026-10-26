import os
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')
if len(SECRET_KEY) < 50:
    raise ImproperlyConfigured('Set DJANGO_SECRET_KEY to a new random secret of at least 50 characters')
DEBUG = os.environ.get('DJANGO_DEBUG') == '1'
ALLOWED_HOSTS = [v.strip() for v in os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1,[::1]').split(',') if v.strip()]
INSTALLED_APPS = ['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','notes']
MIDDLEWARE = ['django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware']
ROOT_URLCONF = 'journal.urls'
TEMPLATES = [{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'templates'],'APP_DIRS':True,'OPTIONS':{'context_processors':['django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION = 'journal.wsgi.application'
DATABASES = {'default':{'ENGINE':'django.db.backends.sqlite3','NAME':os.environ.get('JOURNAL_DB', BASE_DIR/'journal.sqlite3')}}
AUTH_PASSWORD_VALIDATORS = [{'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},{'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator'},{'NAME':'django.contrib.auth.password_validation.CommonPasswordValidator'},{'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator'}]
LANGUAGE_CODE = 'it-it'
TIME_ZONE = 'Europe/Rome'
USE_TZ = True
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR/'staticfiles'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = os.environ.get('DJANGO_SECURE_COOKIES') == '1'
CSRF_COOKIE_SECURE = SESSION_COOKIE_SECURE
