import time

file = None
try:
    file = open('test.txt', mode='r', encoding='UTF-8')
    while True:  # our usual file-reading idiom
        line = file.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2)  # To make sure it runs for a while
except FileNotFoundError as fe:
    print(fe)
except KeyboardInterrupt:
    print('!! You cancelled the reading from the file.')
finally:
    if file is not None:
        file.close()
        print('(Cleaning up: Closed the file)')
