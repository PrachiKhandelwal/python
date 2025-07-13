import os

try:
    curDirectory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(curDirectory)
    # f = open('os.tx')
    f = open('test.txt')
    # we can raise exceptions manually as well
    f_extension=os.path.splitext(f.name)[1]
    if f_extension != '.txt':
        raise Exception('File needs to be a .txt file')
# keep the specific exceptions first and general exceptions towards the end
except FileNotFoundError as e:
    print('File Not found',e)
except Exception as e:
    print(e)
else:
    # else block runs if try block executes successfully
    f_contents = f.read()
    print(f_contents)
finally:
    # finally blocks no matter what
    # usecase  includes releasing resources, close db connections, etc
    print('inside finally')