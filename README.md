# psycopg2-seg-fault-investigation

-u postgres

docker run --network=host \
-e POSTGRES_PASSWORD=postgres \
-v $PWD/tmp-db:/var/lib/postgresql/data \
postgres:17.2-bullseye


https://goteleport.com/learn/postgresql-ssl-authentication-guide/

openssl genrsa -des3 -out server.key 2048
securepassword
openssl req -new -key server.key -out server.csr

Common Name: ???
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt 

add below to postgres conf
ssl_passphrase_command = 'echo "securepassword"'

cp server.* tmp-db

docker run -it --network=host \
-w /opt/workdir -v $PWD:/opt/workdir tensorflow/tensorflow:2.21.0 bash

pip install psycopg2-binary

python foobar.py