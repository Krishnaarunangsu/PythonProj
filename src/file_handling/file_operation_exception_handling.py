class FileHandling:
    """
    File Handling class
    """

    def __init__(self):
        """
        Initialization
        """
        self.file_name = None
        self.file = None

    def read_file(self, file_name: str):
        self.file_name = file_name
        try:
            self.file = open(file_name, encoding='utf-8')
            # perform file operations
        except FileNotFoundError as fe:
            print(fe)
        finally:
            if self.file:
                self.file.close()


file_handling = FileHandling()
file_handling.read_file('poem.txt')
