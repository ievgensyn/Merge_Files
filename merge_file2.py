import datetime
import glob2

"""
This script creates a new text file and then iterate through the file list
inside that "with" statement and open and read existing file contents in each iteration 
and write them to new text file with time-stamp as the filename.
"""

lst = glob2.glob('*.txt')
filename = datetime.datetime.now()


def create_file():
    with open(filename.strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", 'w') as file:
        for item in lst:
            with open(item, 'r') as cont:
                #content = cont.read() -- this line was at first,
                                        # and the next line was: file.write(content + '\n')
                file.write(cont.read() + '\n')


create_file()
