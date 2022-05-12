from mysql.connector import connect

from src.utilities import load_json_data


class DatabaseConnection:
    """

    """

    def __init__(self):
        """

        """
        self.db_config_data = None
        self.connection = None

    def create_connection(self):
        """

        :return:
        """
        self.db_config_data = load_json_data.LoadJSON()  # Instantiate the LoadJSON Object

        # Get the DB Configurations Data from the json file
        config = self.db_config_data.load_json_data_from_file('db_config.json')
        print(f'DB Configurations:{config}')
        with connect(**config) as connection:
            if connection.is_connected():
                print('HIIIIIIIIIIIIIIIIIII')
                self.connection = connection
                print(f'Hi:{self.connection}')
                db_Info = connection.get_server_info()
                print('***************************************')
                print("Connected to MySQL Server version ", db_Info)
                print('***************************************')
                print(f'Connection Info:{self.connection.cursor()}')
                print('***************************************')
        return self.connection
