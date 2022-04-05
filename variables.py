import os

host = os.environ['AZURE_DATABASE_HOST']
user = os.environ['AZURE_DATABASE_USER']
password = os.environ['AZURE_DATABASE_PASSWORD']
database = os.environ['AZURE_DATABASE_DB']
ssl_ca = os.environ['AZURE_DIGITAL_CERTIFICATE_PEM']


def display():
    print("host: " + host)
    print("user: " + user)
    print("password: " + password)
    print("database: " + database)
    print("ssl_ca: " + ssl_ca)
