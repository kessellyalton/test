from pathlib import Path
import os
from decouple import config, Csv
from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv(), default=['innohubliberia.com'])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mysite.apps.MysiteConfig',
    'django_ckeditor_5',
    'crispy_forms',
    'crispy_bootstrap4',
    'django_plotly_dash',
]

MIDDLEWARE = [
    'django_plotly_dash.middleware.BaseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

ROOT_URLCONF = 'innohub_website.urls'

# Switch to SQLite for database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # SQLite backend
        'NAME': BASE_DIR / 'db.sqlite3',  # Path to SQLite file in the project directory
    }
}

# Template Configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Add templates directory if you have custom templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Ensure this points to the correct directory
STATIC_ROOT = BASE_DIR / 'staticfiles'  # For collecting static files during deployment
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'




EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = 'kessellyalton1@gmail.com'

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link', 'bulletedList', 'numberedList', 'blockQuote'],
        'height': 300,
        'width': 'auto',
        'removePlugins': ['MediaEmbed', 'Table'],
        'language': 'en',
    },
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}

PLOTLY_DASH = {
    "ws_route": "ws/channel",
    "http_route": "http/channel",
    "cache_timeout": 60,
}

X_FRAME_OPTIONS = "SAMEORIGIN"
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

FOURSQUARE_API_KEY = config('FOURSQUARE_API_KEY')
