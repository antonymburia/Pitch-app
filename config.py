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



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
        
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
   
    
    


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