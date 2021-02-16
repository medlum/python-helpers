## This helper function is useful to rename multiple files with long filenames

### How to use this helper function

import os
import re
from os import path
from helper_rename_file import convert_name, rename_file

textfile = 'C:/Users/John/Documents/file.txt'
path = 'C:/Users/John/Documents/Folder'

convert_name(textfile = textfile, extension = 'rmd')
rename_file(path = path)