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
    SQLALCHEMY_DATABASE_URI = 'postgresql://nsigjrvudysqnn:92d46f0fb5d0c995e03a73d38697daaa3bb0fad485c87132a3192a9378de7115@ec2-54-156-110-139.compute-1.amazonaws.com:5432/debdkkrsfugedb'
    
   



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
        
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql://nsigjrvudysqnn:92d46f0fb5d0c995e03a73d38697daaa3bb0fad485c87132a3192a9378de7115@ec2-54-156-110-139.compute-1.amazonaws.com:5432/debdkkrsfugedb'
    

    
   
   
    
    


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