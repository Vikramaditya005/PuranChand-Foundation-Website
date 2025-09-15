

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-4&*0w_u(-8=%g7u@+zye)wo_7!yy_^&w=e$4&wak_a0vr&dfl#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = [
    os.environ.get("RENDER_EXTERNAL_HOSTNAME", ""),
    "127.0.0.1",
    "localhost",
    ".ngrok-free.app",
    "puranchandfoundation.org",
    "www.puranchandfoundation.org",
    ".onrender.com",
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'foundation_app',
    'cloudinary',
    'cloudinary_storage',
]

# ---------------- Cloudinary ---------------- #
# Use environment variables, not raw keys here
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('drjrioej8'),
    'API_KEY': os.getenv('737519398591391'),
    'API_SECRET': os.getenv('CKaHFiL2ICjCkp-GGbwOoNxYdfk'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# ------------------------------------------------ #


ROOT_URLCONF = 'PCF.urls'

# foundation_project/settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'foundation_app.context_processors.current_year', # Add this for current_year
            ],
        },
    },
]

WSGI_APPLICATION = 'PCF.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Razorpay credentials
RAZORPAY_KEY_ID = "rzp_live_RHnSL3uXGp6LQi"
RAZORPAY_KEY_SECRET = "L57ESuS8DQT4Xb0xXaHHioP2"
# Redirects for login/logout
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'   # after successful login
LOGOUT_REDIRECT_URL = '/'            # after logout
