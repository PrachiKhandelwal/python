def fun1():
    pass #use  pass if we dont want to define the function definition as of now

# parameters are passed by value for immutable data types (intefger, float, string)

# parameters are passed by reference for mutable data types (list, dictionary, set)

# The tuple itself is immutable, but it can hold mutable elements like a list and those can be modified inside the function and this is reflected outside the function too.

def greet(name='you'):
    print(f'hello {name}')

greet('prachi')

def sum(num1,num2):
    return num1 + num2

print(sum(1.4,2.664))

'''

*args - tuple containing all the positional arguments
**kwargs - dictionary containing all keyword (key-value pair) arguments
we can use both *args and **kwargs in same function definition but *args should come before **kwargs

'''

def student_info(*args, **kwargs):
    print(f'args: {args}, kwargs: {kwargs}')

student_info('math','art',name='riya',semester=1)

# arguments unpacking - unpack iterables like list, tuples, set using *; unpack dictionary using **  
course_info = ['math','art','history']
info = {'name':'priya','semester':1}
student_info(*course_info,**info)