from mysql.connector import connect, Error

from src.utilities import load_json_data

db_config_data = load_json_data.LoadJSON()
config = db_config_data.load_json_data_from_file('db_config.json')

# config = {
#     'user': 'scott',
#     'password': 'password',
#     'host': '127.0.0.1',
#     'database': 'employees',
#     'raise_on_warnings': True
# }

try:
    with connect(
            **config
    ) as connection:
        print(connection)
except Error as e:
    print(e)

# try:
#     with connect(
#             host="localhost",
#             # user=input("Enter username: "),
#             # password=getpass("Enter password: "),
#             user='root',
#             password='Narayan@15',
#     ) as connection:
#         print(connection)
# except Error as e:
#     print(e)
