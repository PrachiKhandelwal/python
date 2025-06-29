language='python'

if language == 'Java':
    print('Java is used')
elif language == 'python':
    print('python is used')
else:
    print('language not found')

# and, or, not operator

user="Admin"
logged_in = False

if user == 'Admin' and logged_in:
    print('welcome')
elif not logged_in:
    print('plese login')
else:
    print('not authorized')

# while using ==, order matters in case of lists and tuples but not in case of dictionary 

l1=[1,2,3,6,4]
l2=[1,2,3,6,4]
l3=l2

print(l1 == l2)

# to check whether two variables point to same memory location, we use 'is' opeartor
print(l1 is l2)
print(l3 is l2)
print(id(l1))
print(id(l2))
print(id(l3))

# false values in python
# False, None, numeric zero, empty string, empty dictionary, empty list, empty tuple, empty set 