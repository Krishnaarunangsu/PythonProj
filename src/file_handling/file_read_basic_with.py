# Python Code to illustrate with


class FileHandling:
    """
    File Handling class
    """

    def __init__(self):
        """
        Initialization
        """
        self.file_name = None
        self.file_data = None

    def read_file(self, file_name: str):
        self.file_name = file_name
        try:
            with open(self.file_name) as file_read:
                self.file_data: str = file_read.read()
        except FileNotFoundError as fe:
            print(fe)
            print('File Does Not Exist')
        finally:
            return self.file_data


file_handling = FileHandling()
text_data: str = file_handling.read_file('poem.txt')
print(f'File data:{text_data}')
