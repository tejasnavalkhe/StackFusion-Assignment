import os

class Config:
    TESTING_SERVER = True
    SECRET_KEY = 'edb7cc4066fd63bdef03d3af978639202634aa8ce32e2a8842c702673220e07f36a0d0ad6bdbf10987877e88ac7eedb7e7c6'
    APP_Id = '56dec554b6'
    APP_SECRET = '3bb59b3a2953acae7780657b6946aac479236f6dd23605e6eeabeaeca2ad38e5'

    if TESTING_SERVER:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///StackFusion.db'
    else:
        SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/StackFusion'

    # Mail Settings
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('email_address')
    MAIL_PASSWORD = os.getenv('email_password')
