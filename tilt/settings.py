import os
import dj_database_url

################################################################################
# Standard Variables
################################################################################
APP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
DEBUG = int(os.environ.get('DEBUG', default=0))
ENVIRONMENT = os.environ.get('ENVIRONMENT', default='production')
TILT_APP = os.environ.get('TILT_APP', default='development')
SECRET_KEY = os.environ.get('SECRET_KEY')


################################################################################
# AWS Variables
################################################################################
AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY', default='none')
AWS_BUCKET = os.environ.get('AWS_BUCKET', default='none')
AWS_LAMBDA_FUNCTION = os.environ.get('AWS_LAMBDA_FUNCTION', default='none')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY', default='none')
AWS_REGION = os.environ.get('AWS_REGION', default='none')
GRAPHQL_ENDPOINT = os.environ.get('GRAPHQL_ENDPOINT', default='none')


################################################################################
# Database certificate files
################################################################################
CA_CERT_PATH = f".postgresql/{TILT_APP}/ca-cert.pem"
CLIENT_CERT_PATH = f".postgresql/{TILT_APP}/client-cert.pem"
CLIENT_KEY_PATH = f".postgresql/{TILT_APP}/client-key.pem"

################################################################################
# Google Variables
################################################################################
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY', default='none')


################################################################################
# Sendgrid Variables
################################################################################
FROM_EMAIL = os.environ.get('FROM_EMAIL', default='hello@tiltaccess.com')
SENDER_NAME = os.environ.get('SENDER_NAME', default='Tilt')
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
SENDGRID_DOMAIN = os.environ.get('SENDGRID_DOMAIN', default='http://localhost:3000')


################################################################################
# Sendgrid Variables
################################################################################
SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
SLACK_SIGNING_SECRET = os.environ.get('SLACK_SIGNING_SECRET')
if TILT_APP == 'production':
    SLACK_AWARD_CHANNEL = '#award-letters-production'
else:
    SLACK_AWARD_CHANNEL = '#award-letters-staging'

################################################################################
# Twilio Variables
################################################################################
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', default='none')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', default='none')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER', default='none')


################################################################################
# Application definition
################################################################################
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'corsheaders',

    # 3rd-party apps
    'graphene_django',
    'social_django',
    'django_better_admin_arrayfield',

    # local
    'financial_aid.apps.FinancialAidConfig',
    'colleges.apps.CollegesConfig',
    'organizations.apps.OrganizationsConfig',
    'scholarships.apps.ScholarshipsConfig',
    'users.apps.UsersConfig',
]

MIDDLEWARE = [
    "django_samesite_none.middleware.SameSiteNoneMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tilt.urls'

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

WSGI_APPLICATION = 'tilt.wsgi.application'


################################################################################
# Database
################################################################################
# database for development without SSL
if ENVIRONMENT == 'development':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DATABASE_NAME'),
            'USER': os.environ.get('DATABASE_USER'),
            'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
            'HOST': os.environ.get('DATABASE_HOST'),
            'PORT': 5432,
        }
    }
# database for staging and production with SSL
if ENVIRONMENT == 'production':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DATABASE_NAME'),
            'USER': os.environ.get('DATABASE_USER'),
            'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
            'HOST': os.environ.get('DATABASE_HOST'),
            'PORT': 5432,
            'OPTIONS':{
                'sslmode':'verify-ca'
                # 'sslcert': CLIENT_CERT_PATH,
                # 'sslkey': CLIENT_KEY_PATH,
                # 'sslrootcert': CA_CERT_PATH
            }
        }
    }

# for heroku
db_from_env = dj_database_url.config(conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)

################################################################################
# Password Validation
################################################################################
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
]


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8, }
    },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'tilt.validators.NumberValidator', },
    {'NAME': 'tilt.validators.UppercaseValidator', },
    {'NAME': 'tilt.validators.LowercaseValidator', },
    {'NAME': 'tilt.validators.SymbolValidator', },
]


################################################################################
# Internationalization
################################################################################
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = True
USE_L10N = True


################################################################################
# Authentication
################################################################################
AUTHENTICATION_BACKENDS = [
    # 'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
]
AUTH_USER_MODEL = 'users.User'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SITE_ID = 1

SOCIAL_AUTH_PIPELINE = [
    # Get the information we can about the user and return it in a simple
    # format to create the user instance later. On some cases the details are
    # already part of the auth response from the provider, but sometimes this
    # could hit a provider API.
    'social_core.pipeline.social_auth.social_details',

    # Get the social uid from whichever service we're authing thru. The uid is
    # the unique identifier of the given user in the provider.
    'social_core.pipeline.social_auth.social_uid',

    # Verifies that the current auth process is valid within the current
    # project, this is where emails and domains whitelists are applied (if
    # defined).
    'social_core.pipeline.social_auth.auth_allowed',

    # Checks if the current social-account is already associated in the site.
    'social_core.pipeline.social_auth.social_user',

    # Make up a username for this person, appends a random string at the end if
    # there's any collision.
    'social_core.pipeline.user.get_username',

    # Send a validation email to the user to verify its email address.
    # Disabled by default.
    # 'social_core.pipeline.mail.mail_validation',

    # Associates the current social details with another user account with
    # a similar email address. Disabled by default.
    'social_core.pipeline.social_auth.associate_by_email',

    # Create a user account if we haven't found one yet.
    'social_core.pipeline.user.create_user',

    # Create the record that associates the social account with the user.
    'social_core.pipeline.social_auth.associate_user',

    # Populate the extra_data field in the social record with the values
    # specified by settings (and the default ones like access_token, etc).
    'social_core.pipeline.social_auth.load_extra_data',

    # Update the user record with any changed info from the auth service.
    'social_core.pipeline.user.user_details',
]

SOCIAL_AUTH_DISCONNECT_PIPELINE = [
    # Verifies that the social association can be disconnected from the current
    # user (ensure that the user login mechanism is not compromised by this
    # disconnection).
    'social_core.pipeline.disconnect.allowed_to_disconnect',

    # Collects the social associations to disconnect.
    'social_core.pipeline.disconnect.get_entries',

    # Revoke any access_token when possible.
    'social_core.pipeline.disconnect.revoke_tokens',

    # Removes the social associations.
    'social_core.pipeline.disconnect.disconnect',
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('GOOGLE_KEY', default='')

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('GOOGLE_SECRET', default='')

################################################################################
# Graphene
################################################################################
GRAPHENE = {
    'SCHEMA': 'tilt.schema.schema',
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}


################################################################################
# Security
################################################################################
if TILT_APP == 'production':
    SESSION_COOKIE_DOMAIN = '.tiltaccess.com'
elif TILT_APP == 'staging':
    SESSION_COOKIE_DOMAIN = '.tiltstaging.dev'
else:
    SESSION_COOKIE_DOMAIN = 'localhost'


CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "https://tiltaccess.com",
    "https://www.tiltaccess.com",
    "https://tiltstaging.dev"
]
CSRF_TRUSTED_ORIGINS = [
    "tiltaccess.com",
    "www.tiltaccess.com",
    "tiltstaging.dev",
]
SESSION_COOKIE_SAMESITE = 'lax'

# security for development
if ENVIRONMENT == 'development':
    ALLOWED_HOSTS = [
        '0.0.0.0',
        '127.0.0.1',
        'localhost',
        '.amazonaws.com',
        '.elasticbeanstalk.com',
        '.tiltstaging.dev'
    ]
    CORS_ORIGIN_ALLOW_ALL = True

# security for production
elif ENVIRONMENT == 'production':
    ALLOWED_HOSTS = [
        '0.0.0.0',
        '.amazonaws.com',
        '.elasticbeanstalk.com',
        '.tiltaccess.com',
        '.tiltstaging.com',
        '.tiltstaging.dev',
    ]
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_PRELOAD = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_REFERRER_POLICY = 'same-origin'
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    X_FRAME_OPTIONS = 'DENY'


################################################################################
# Static Files
################################################################################
STATIC_URL = '/static/'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "../", "staticfiles")
