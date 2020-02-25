import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or b'+\xd0\x8e\x93H\x9a\xa2\x10\x10q\xe2\xff\xa8\xe4\xb2\x12\xe7\x97\x1c!\xd61=\x94'
