import os

folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder_path,'test2.txt')

with open(file_path,'w') as f:
    f.write('hello')

with open(file_path, 'w') as f:
    f.write(' hi')
    f.seek(0)
    f.write(' there')


# copy one file content into another file
original_file_path = os.path.join(folder_path, 'test.txt')
copy_file_path = os.path.join(folder_path,'test-copy.txt')

with open(original_file_path,'r') as rf:
    with open(copy_file_path,'w')  as wf:
        for line in rf:
            wf.write(line)

# create a copy of an image file
original_image_path = os.path.join(folder_path,'apple.jpeg')
copy_image_path = os.path.join(folder_path,'apple-copy.jpeg')

with open(original_image_path,'rb') as rbf:
    with open(copy_image_path,'wb') as wbf:
        # for line in rbf:
        #     wbf.write(line)
        chunk_size  = 100
        content = rbf.read(chunk_size)
        while len(content) > 0:
            wbf.write(content)
            content = rbf.read(chunk_size)