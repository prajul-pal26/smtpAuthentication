from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

CSRF_TRUSTED_ORIGINS = ['https://*.cotgen.com','https://127.0.0.1']

SECRET_KEY = 'django-insecure-%0+c=u$s04ro%@_56$n1wmd2)$%-s2h6$hi!8#jcu@=d44@je_'

DEBUG = True

ALLOWED_HOSTS = [
    'db',
    'localhost',
    '127.0.0.1',
    # 'project-hkj0.onrender.com',
    'www.cotgen.com',
    'smtpauthentication.onrender.com',  # <-- add this line

]

INSTALLED_APPS = [
    'app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# For default database-backed session storage
SESSION_ENGINE = 'django.contrib.sessions.backends.db'


ROOT_URLCONF = 'PROJECT.urls'

USE_TZ = True

STATIC_URL = '/static/'   #end point where we have to use the static
STATICFILES_DIRS = (
  'static',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),  # Path to your app's templates folder and
        ],
        'APP_DIRS': True,  # This tells Django to search for static files in app directories
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

WSGI_APPLICATION = 'PROJECT.wsgi.application'
# import os
# from dotenv import load_dotenv
# load_dotenv()

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.getenv("DB_NAME"),
#         "USER": os.getenv("DB_USER"),
#         "PASSWORD": os.getenv("DB_PASSWORD"),
#         "HOST": os.getenv("DB_HOST"),
#         "PORT": os.getenv("DB_PORT"),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
