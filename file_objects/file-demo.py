import os


# __file__ may give relative or absolute path depending on how the file is run
print(__file__)


folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder_path, 'test.txt')

file = open(file_path,'r')
print(file)

# important to close files to avoid leaks
file.close()

# read file using context
with open(file_path,'r') as f:
    # f_contents=f.read()
    # print(f_contents)
    # f_first_line=f.readline()
    # print(f_first_line)
    # f_content_lines=f.readlines()
    # print(f_content_lines)

    '''method 1  to efficiently read file contents from a large file'''
    for line in f:
        print(line,end='')
    f.seek(0) # to update the current position

    '''method 2 to efficiently read file contents from a large file'''
    chunk_size = 20
    f_content = f.read(chunk_size)
    print('\n',f.tell())  # to print the current position
    while len(f_content) > 0:
        print(f_content,end='*')
        print(f.tell())
        f_content=f.read(chunk_size)

    
    