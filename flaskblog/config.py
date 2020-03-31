import os


class Config:
    SECRET_KEY = '4d674dabd9d333c3f8871709655dcabc'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'neerukondapuneeth2018@gmail.com'
    MAIL_PASSWORD = ''
