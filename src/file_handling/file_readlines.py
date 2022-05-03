# Python code to illustrate split() function
with open("C:\\Arunangsu\\Test_Data\\File_Handling\\file_1.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

# read() function reads an entire file, as though it were a string. This means that it treats each character
# differently, so if you were trying to iterate over a file e.g:
#
# file_1 = open('file', 'r')
# for i in file_1.read():
# pass #or code
#
# The .read() would treat each character in the file separately, meaning that the iteration would happen for every
# character.
#
# The readline() function, on the other hand, only reads a single line of the file. This means that if the file
# file_1 were three lines long, the readline() function would only parse (or iterate/operate) on the first line of
# the file.
