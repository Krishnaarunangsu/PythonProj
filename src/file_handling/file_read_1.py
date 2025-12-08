class FileReader:
    """
    Class for Reading a file
    """
    def __init__(self, file_name:str):
        """
        Initialization
        :param file_name:
        """
        self.file_name=file_name
        self.raw_text=""

#    @property
    def read_file(self):
        """
        Read the Raw Text from the file
        :return:
        """
        try:
            with open(self.file_name,'r') as file:
                self.raw_text=file.read()
                print(f"The File content is:{self.raw_text}")
        except FileNotFoundError as fe:
            #print(f"{self.file_name} Not Found",fe)
            print(fe)
        finally:
            return self.raw_text

if __name__=="__main__":
    file_name="C:\\Arunangsu\\Test_Data\\file_2.txt"
    file_reader=FileReader(file_name)
    raw_data=file_reader.read_file()