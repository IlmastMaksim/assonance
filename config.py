import os

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:persik@localhost:5432/assonance" #os.getenv("DATABASE_URL")

SECRET_KEY = "95d3763bb55e744e77dd181a47b4e1c6" #os.getenv("SECRET_KEY")

DEBUG = True
 
SQLALCHEMY_TRACK_MODIFICATIONS = True

DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 2

ERROR_404_HELP = False

CSRF_ENABLED = True