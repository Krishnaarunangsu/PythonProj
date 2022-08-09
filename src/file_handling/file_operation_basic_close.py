class FileHandling:
    """
    File Handling class
    """
    def __init__(self):
        """
        Initialization
        """
        self.file_name = None

    def read_file(self, file_name: str):
        # making the file name available throughout the class
        self.file_name = file_name

        # Open and Read the file
        file = open(file_name, mode='r', encoding='utf-8')  # with encoding
        print(file.read())
        file.close()


file_handling = FileHandling()
file_handling.read_file('test.txt')
