from __future__ import absolute_import, unicode_literals
from .base import *
import dj_database_url
import os


DATABASES['default'] = dj_database_url.config()


env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']
AWS_STORAGE_BUCKET_NAME = env['AWS_STORAGE_BUCKET_NAME']
AWS_S3_REGION_NAME = env['AWS_S3_REGION_NAME']
AWS_ACCESS_KEY_ID = env['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = env['AWS_SECRET_ACCESS_KEY']

AWS_S3_CUSTOM_DOMAIN = env['AWS_S3_CUSTOM_DOMAIN']
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# DO NOT DO THIS!
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3Boto3Storage'

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'

# Allow all host headers
ALLOWED_HOSTS = ['*']
DEBUG = False

try:
    from .local import *
except ImportError:
    pass
