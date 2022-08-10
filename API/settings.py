import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'u@2i##k+)vys^g&vy!y2nbyy+h@*zpvw@y+k1=r5yl(i8t3628'

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'rest_auth',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'django_filters',
    'colorfield',
    'multimoneda.apps.MultimonedaConfig',
    'industrialgip.apps.IndustrialgipConfig',
    ]
SITE_ID = 1

#MEDIA_ROOT='/media/'

#MEDIA_URL='/media/'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'API.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


WSGI_APPLICATION = 'API.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        #'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
       'DEFAULT_PERMISSION_CLASSES': (
      #'rest_framework.permissions.IsAuthenticated',
       'rest_framework.permissions.AllowAny',
    ),
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'helpcomdb',
#        'USER': 'postgres',
#        'PASSWORD': '12345',
#        'HOST': 'localhost',
#        'PORT': 5432,
#    }
#}
DATABASES = {
        'default':{
            'ENGINE': 'sql_server.pyodbc',
            'NAME': 'apidb',
            'USER': 'sa',
            'PASSWORD': '123456Ps',
            'HOST': '172.19.48.17',
            'PORT': '32139',
            'OPTIONS': {
                'driver': 'ODBC Driver 17 for SQL Server'
                },
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

ACCOUNT_LOGOUT_ON_GET = True


CORS_ALLOW_HEADERS = ( 
    'x -request-with ', 
    ' content-type ', 
    ' accept ', 
    ' origin ', 
    ' authorization ', 
    ' x-csrftoken ', 
    ' Api-Authorization ', 
)
CORS_ORIGIN_ALLOW_ALL = True


LANGUAGE_CODE = 'es-ve'

TIME_ZONE = 'America/Antigua'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

STATIC_URL = '/static/'

JAZZMIN_SETTINGS = {
   "site_title": "Administracion GIP",
   "site_logo": "media/logoname.png",
   "welcome_sign": "Inicio de sesión",
   "site_icon": "media/favicon-32x32.png",
   "site_logo_classes": "no-border",
   "copyright": "Grupo Industrial Polybarq",
   "search_model": "auth.User",
   "show_ui_builder": True
}
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": True,
    "sidebar_nav_small_text": True,
    "brand_colour": False,
    "accent": "accent-lightblue",
    "navbar": "navbar-lightblue navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-light-lightblue",
    "sidebar_disable_expand": True,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": False,
    "theme": "sandstone",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    }
}