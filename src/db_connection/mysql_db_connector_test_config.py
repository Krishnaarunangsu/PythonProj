import mysql.connector

from getpass import getpass
from mysql.connector import connect, Error

config = {
    'user': 'root',
    'password': 'Narayan@15',
    'host': '127.0.0.1',
    'database': 'narayan',
    'raise_on_warnings': True
}

# cnx = mysql.connector.connect(**config)

try:
    with connect(
            **config
    ) as connection:
        print(connection)
except Error as e:
    print(e)
