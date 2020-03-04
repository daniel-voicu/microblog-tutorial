import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or b'+\xd0\x8e\x93H\x9a\xa2\x10\x10q\xe2\xff\xa8\xe4\xb2\x12\xe7\x97\x1c!\xd61=\x94'

    MAIL_SERVER = os.environ.get('MAIL_SERVER') or "smtp.googlemail.com"
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or None
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or None
    ADMINS = ["notifications.script@gmail.com"]

    POSTS_PER_PAGE = 3

    LANGUAGES = ['en', 'es']

    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
