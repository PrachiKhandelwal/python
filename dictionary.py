student={'name':'prachi','courses':['math','english','physics']}

print(student['name'])

# dictionary keys must be unique and immutable

# trying to access a non-existent key results in key error
# print(student['phone'])

# if we want to get 'None' or a default value if key does not exist, we can use get() method
print(student.get('phone'))
print(student.get('phone','Not Found'))

#  to add new key value pair
student['phone']='9622990012'
print(student.get('phone'))

# to update existing value
student['name']='Prachi K'
print(student['name'])

# to add/update multiple values
student.update({'name':'Lana','age':23})
print(student)

# delete a key value pair
del student['age']
print(student)

courses=student.pop('courses')
print(f'{student}, {courses}')

# to get number of keys
print(len(student))

# to get all keys
print(student.keys()) 

# to get all values
print(student.values())

# to get both key and value
print(student.items())

# loop over dictionary

for key, value in student.items():
    print(f'{key}: {value}')