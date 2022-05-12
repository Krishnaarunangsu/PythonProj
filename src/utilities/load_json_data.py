import json
from pprint import pprint


class LoadJSON:
    """
    Loads JSON
    """

    def __init__(self):
        """

        """
        self.file_name = None
        self.json_data = None

    def load_json_data_from_file(self, db_config_file):
        """

        :return:
        """
        self.file_name = db_config_file
        # with open('..\\db_connection\\db_config.json') as db_config:
        with open(self.file_name) as db_config:
            self.json_data = json.load(db_config)
            pprint(self.json_data)
            return self.json_data

# load_json = LoadJSON()
# load_json.load_json_data_from_file('..\\db_connection\\db_config.json')
