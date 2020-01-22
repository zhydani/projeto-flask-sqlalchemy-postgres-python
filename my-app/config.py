#from os import environ

class Config:
    # Database
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:123456@localhost:5432/transparencia"
    SQLALCHEMY_TRACK_MODIFICATIONS = False