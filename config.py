import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'latifa-srv.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'latifa'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'latifa'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'P@ssw0rd'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'latifastorage'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '9W0LwjBOqwEw2yeDwwd/IglH36qHPkg6ZQIQcNPNDvAnSAkDxkjVoTmMYkID4zfQ+imi9zCdD+Mf5o7dSNDKIQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'myimages'
