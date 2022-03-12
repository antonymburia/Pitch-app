import os
import re

class Config:
    '''
    General configuration parent class
    '''

    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = 'thisissecretkey'
    

    #email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_DATABASE_URI = 'postgres://ynknhnrzzvnbmr:345042093ed841f20699836d261ac6716e0dadd25944bc523aa0dbde12920921@ec2-54-80-137-25.compute-1.amazonaws.com:5432/dd5q95lbq07p3t'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
        
    '''
    SQLALCHEMY_DATABASE_URI = 'postgres://ynknhnrzzvnbmr:345042093ed841f20699836d261ac6716e0dadd25944bc523aa0dbde12920921@ec2-54-80-137-25.compute-1.amazonaws.com:5432/dd5q95lbq07p3t'
   
   
    
    


class DevConfig(Config):
    '''
    Development  configuration child class 

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitchapp'
  

    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}