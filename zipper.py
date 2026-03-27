import os
from shutil import rmtree, move, make_archive

timestozip = int(input("How many times must I zip the file >>>"))

filename = input("Please input the file to be zipped here >>>")

zipname = filename.split(".")[0] + ".zip"

foldername = filename.split(".")[0]

current_file = filename

for i in range(timestozip):
    os.mkdir(foldername)
    move(current_file, foldername)
    make_archive(foldername, 'zip', '.', foldername) 
    rmtree(foldername)
    current_file = zipname

# make the dir
# move the file in the dir
# make the zip
# remove the folder
# make the thing like loop back to move the zip in the folder

