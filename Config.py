import os

class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'postgresql://pqmccpblfjavhq:a2989bfbecc484ad4f80f653a367dcadb29b9d910c57ef40d256aff2c01deda1@ec2-52-45-183-77.compute-1.amazonaws.com:5432/d4oiit10qncdof'

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True