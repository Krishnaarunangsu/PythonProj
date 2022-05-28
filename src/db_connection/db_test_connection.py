from mysql.connector import connect, Error

from src.utilities import load_json_data


# config = {
#     'user': 'root',
#     'password': 'Narayan@15',
#     'host': '127.0.0.1',
#     'database': 'narayan',
#     'raise_on_warnings': True
# }

class DatabaseConnection:
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
            with connect(**self.config) as connection_obj:
                if connection_obj.is_connected():
                    self.connection = connection_obj
            return self.connection

        except Error as e:
            print(e)


if __name__ == "__main__":
    crud = DatabaseConnection()
    connection = crud.perform_CRUD()
    print(connection)
