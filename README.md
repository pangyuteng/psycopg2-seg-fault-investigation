
# psycopg2-seg-fault-investigation


```

https://github.com/psycopg/psycopg2/issues/543

libpq libssl

https://stackoverflow.com/questions/2011578/can-i-find-out-where-a-python-application-crashed-using-the-data-dump

-u postgres

docker run --network=host \
-e POSTGRES_PASSWORD=postgres \
-v $PWD/tmp-db:/var/lib/postgresql/data \
postgres:17.2-bullseye


https://goteleport.com/learn/postgresql-ssl-authentication-guide/

openssl genrsa -des3 -out server.key 2048

securepassword

openssl req -new -key server.key -out server.csr

Common Name: abc.com

openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt 

sudo cp server.* tmp-db/

add below to postgres conf
ssl_passphrase_command = 'echo "securepassword"'

cp server.* tmp-db

docker run -it --network=host \
-w /opt/workdir -v $PWD:/opt/workdir tensorflow/tensorflow:2.21.0 bash

pip install psycopg2-binary

python foobar.py

# if `import tensorflow` comes before `import psycopg2`, you get segmentation fault

ldd /usr/local/lib/python3.11/dist-packages/psycopg2/_psycopg.cpython-311-x86_64-linux-gnu.so

find / -name "libpq*"

find / -name "libssl*"


```

<img width="1498" height="311" alt="image" src="https://github.com/user-attachments/assets/87f171e5-d108-4f15-a9b8-5f20de827fe6" />

<img width="1500" height="481" alt="image" src="https://github.com/user-attachments/assets/16063669-078f-4ef8-b83e-f18a1efe489a" />

<img width="897" height="310" alt="image" src="https://github.com/user-attachments/assets/cc639cac-f86f-4070-9030-217e88778f75" />
