import os
import re
from os import path

def convert_name(textfile, extension):
    
    ''' This function replace whitespace with underscore and add a file extension.
    It takes 2 arguments:
    1. A .txt file which consists of student names to be in 1 column with n rows. 
    2. Extension argument for the file type. It requires quotation.
    Example: convert_name(filepath = c:/Users/John/Document/class.txt, extension = 'doc')
    '''
       
    global className
    names = []
    class_list = []    
        
    with open(textfile, 'r') as reader:
        names = [i for i in reader.readlines()]
    
    class_names = [''.join(x) for x in names]

    for name in class_names:
        class_list.append(re.sub('\W', "_", name))

    className = [name + '.' + '{}'.format(extension) for name in class_list]
    
    return className

def rename_file(path):
    
    ''' This function rename file names in a folder.
    It takes 1 argument:
    1. Folder path where the files are located.
    Example: rename_file(path = c:/Users/John/Document/Folder)
    '''
    assignment_file = os.listdir(path)
    for f, b in zip(assignment_file, className):
        os.rename(os.path.join(path , f), os.path.join(path, b))
