from mysql.connector import connect, Error

from db_test_connection import CRUDOperation


# config = {
#     'user': 'root',
#     'password': 'Narayan@15',
#     'host': '127.0.0.1',
#     'database': 'narayan',
#     'raise_on_warnings': True
# }

class CRUDOperation():
    """

    """

    def __init__(self):
        """

        """
        self.db_config_data = None
        self.config = None

    def perform_CRUD(self):
        """

        :return:
        """
        try:
            self.db_config_data = load_json_data.LoadJSON()
            self.config = db_config_data.load_json_data_from_file('db_config.json')
            print(f'DB Configurations:{config}')
            with connect(**config) as connection:
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


if __name__ == "__main__":
    crud = CRUDOperation()
    crud.perform_CRUD()
