import os
import shutil
path = "./"
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.find("2020142149") != -1]

for files in file_list_py:
    shutil.move(files, '1학년 1학기')
