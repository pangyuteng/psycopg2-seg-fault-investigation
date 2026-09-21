
import faulthandler
faulthandler.enable()

import tensorflow
import psycopg2

connection = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/postgres")
connection.set_client_encoding('utf8')
print(connection)

connection = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/postgres?sslmode=require")
connection.set_client_encoding('utf8')
print(connection)