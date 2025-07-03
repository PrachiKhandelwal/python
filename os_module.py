import os
from datetime import datetime

# to get currrent working directory
print(os.getcwd())

# to get details about a file/folder
print(os.stat('os_module.py'))

# to get date from timestamp
modified_time = datetime.fromtimestamp(os.stat('os_module.py').st_mtime)
print('last modified time: ',modified_time)

# to get all methods available in os module 
# print(dir(os))

# to list the tree (files and folders) for a directory
for dirpath, dirnames, filenames in os.walk('.'):
    print('current path: ',dirpath,', folders: ',dirnames,' filenames: ',filenames)

# to read environment variables
home_dir = os.environ.get('HOME')
print('home directory: ',home_dir)

# to get file absolute path
path=os.path.join(os.getcwd(),'sample.txt')
print('path: ',path)

# to get last part (file or folder) of a path
print(os.path.basename('/user/tmp/notes.txt'))

print(os.path.dirname("/home/user/folder/"))

print(os.path.exists('/tmp/prachi'))

#  to check if the path exists and whether the path is a directory
print(os.path.isdir('C:\\Users\\Hp\\Desktop'))

# to grab extension of a file
print(os.path.splitext('test/abc.py'))

# usecase: when we want to change directory for calculating relative path
os.chdir('C:\\Users\\Hp\\Desktop')

print(os.getcwd())

# to list the files and folders  in current working directory
print(os.listdir())

# to create a folder
os.mkdir('test_folder')

# to create nested folder (creates intermediate folders if they don't exist yet)
os.makedirs('nested/test')  # prefer this while creating directory

# to rename a file or folder
os.rename('test_folder','new_folder')

# used to delete a folder
# raises error if test_folder is non empty
os.rmdir('new_folder')

# deletes c, followed by b (only if b is empty), followed by a (only if a is non empty) 
# raises error if c is non empty
os.removedirs('a/b/c') 
