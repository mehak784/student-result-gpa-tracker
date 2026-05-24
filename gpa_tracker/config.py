import os

class Config:
    SECRET_KEY = 'mysecretkey123'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///students.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False