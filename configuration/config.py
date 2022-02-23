from distutils.debug import DEBUG


import os

class Config(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(object):
    ENV="development"
    DEBUG = True
    ZD_AUTH_USER = os.environ.get('ZD_AUTH_USER')
    ZD_AUTH_PASSWORD = os.environ.get('ZD_AUTH_PASSWORD')