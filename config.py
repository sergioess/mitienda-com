import os
import psycopg2

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'postgresql://oxwttxarfidlxi:89e47cacfc5926776ab52a7e485b08a91bf9632736ca0843d80b6356b506f3f2@ec2-3-231-69-204.compute-1.amazonaws.com:5432/d3hr8qndm4p50h'
SQLALCHEMY_TRACK_MODIFICATIONS = False

CARPETA_IMG = os.path.join('img')
CARPETA_PTOS = os.path.join('uplproductos')


MAIL_SERVER='smtp.gmail.com'
MAIL_PORT=587
MAIL_USERNAME = 'mitiendamintic@gmail.com'
MAIL_PASSWORD = '3nviodeCorr3oPython'
MAIL_USE_TLS = True
MAIL_USE_SSL = False

SESSION_TYPE = "filesystem"
SESSION_PERMANENT = False

