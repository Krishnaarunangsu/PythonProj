from mysql.connector import connect, Error

from db_test_connection import DatabaseConnection
from src.utilities import load_json_data


# db_config_data = load_json_data.LoadJSON()
# config = db_config_data.load_json_data_from_file('db_config.json')
# print(f'DB Configurations:{config}')


# config = {
#     'user': 'root',
#     'password': 'Narayan@15',
#     'host': '127.0.0.1',
#     'database': 'narayan',
#     'raise_on_warnings': True
# }

class CRUDOperation:
    """

    """

    def __init__(self):
        """

        """
        self.db_config_data = None
        self.config = None
        self.connection = None

    def perform_CRUD(self):
        """

        :return:
        """
        try:
            self.db_config_data = load_json_data.LoadJSON()
            self.config = self.db_config_data.load_json_data_from_file('db_config.json')
            print(f'DB Configurations:{self.config}')
            with connect(**self.config) as connection:
                if connection.is_connected():
                    db_Info = connection.get_server_info()
                    print('***************************************')
                    print("Connected to MySQL Server version ", db_Info)
                    print('***************************************')
                    print(f'Connection Info:{connection}')
                    print('***************************************')
                    print(f'Cursor:{connection.cursor()}')
                    select_db_query = "SELECT * FROM Persons"
                    with connection.cursor() as cursor:
                        cursor.execute(select_db_query)
                        for db in cursor:
                            print(f'Database Records:{db}')
        except Error as e:
            print(e)

    def perform_db_operation(self):
        """

        :return:
        """
        try:
            db_connection = DatabaseConnection()
            self.connection = db_connection.perform_CRUD()
            print(f'Connection:{self.connection}')
            # print(f'Cursor:{self.connection.cursor()}')
            select_db_query = "SELECT * FROM Persons"
            with self.connection as conn:
                print(conn.cursor())

        except Error as e:
            print(e)
        finally:
            print('It is done')


if __name__ == "__main__":
    crud = CRUDOperation()
    crud.perform_CRUD()
