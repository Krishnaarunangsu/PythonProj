import mysql.connector
from mysql.connector import errorcode
from mysql.connector import (connection)

import mysql.connector

cnx = mysql.connector.connect(user='scott', password='password',
                              host='127.0.0.1',
                              database='employees')
cnx.close()

try:
    cnx = mysql.connector.connect(user='scott',
                                  database='employ')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()

cnx = connection.MySQLConnection(user='scott', password='password',
                                 host='127.0.0.1',
                                 database='employees')
cnx.close()

x = 'Krishna'
config = {
    'user': 'scott',
    'password': 'password',
    'host': '127.0.0.1',
    'database': 'employees',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cnx.close()
