print('importing my module...')

test = 'Test string'

def find_index(seachItem,arr):
    for idx,value in enumerate(arr):
        if(seachItem == value):
            return idx
    return -1