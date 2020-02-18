import os

class Config:

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
     '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}