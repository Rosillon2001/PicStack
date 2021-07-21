import os

class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'postgresql://iayghclllpftmr:372f6316d6b7513808eb091ddf55432bb2c6498630446be4d7eda83d83e319b6@ec2-34-204-128-77.compute-1.amazonaws.com:5432/d4i44hhpgsuss2'

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True