from mysql.connector import Error

from database_connector import DatabaseConnection


class CRUD:
    """

    """

    def __init__(self):
        """

        """
        self.connection = None
        self.database_connection = None
        self.cursor = None

    def fetch_person_data(self):
        try:
            select_db_query = "SELECT * FROM Persons"
            self.database_connection = DatabaseConnection()
            self.connection = self.database_connection.create_connection()
            print(f'Retrieved cursor is:{self.connection}')
            print(f'Hiiiii:{self.connection.cursor()}')
            with self.connection.cursor() as cursor:
                cursor.execute(select_db_query)
                for db in cursor:
                    print(f'Database Records:{db}')
        except Error as e:
            print(e)


if __name__ == "__main__":
    crud = CRUD()
    crud.fetch_person_data()
