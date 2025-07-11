import os

os.chdir('C:\\Users\\Hp\\Desktop\\cs\\project-automating file renaming\\files')

# print(os.path.abspath(os.curdir))

for file in os.listdir():
    if(os.path.isfile(file)):
        filename,extension = os.path.splitext(file)
        planet,commonStr,num=filename.split('-')
        planet = planet.strip()
        num = num.strip()[1:].zfill(2)
        newName = f'{num}-{planet}{extension}'
        os.rename(file, newName)