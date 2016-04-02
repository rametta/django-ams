from collection.settings import *
import dj_database_url

AWS_STORAGE_BUCKET_NAME = 'galleryx'
AWS_ACCESS_KEY_ID = 'AKIAI7TAAKTCHYX3GNIA'
AWS_SECRET_ACCESS_KEY = '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'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

DATABASES['default'] = dj_database_url.config()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
DEBUG = False
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'