import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SULALSEMODALOgY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite://app.db'
    SULALSEMODALOGY_TRANCK_MODIFICATIONS = False