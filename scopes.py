'''
LEGB
local scope
enclosing scope
global scope
built-in scope
'''

'''
LOCAL SCOPE: variables that are defined inside a function, they are accessible within the function only
'''
def greet():
    message = 'hello'
    print(message)

greet()



'''
ENCLOSING SCOPE: In nested functions, inner functions can access variables defined in outer  funnction
'''
def outer():
    num = 1
    def inner():
        num=8
        print('inside: ',num)
    inner()
    print('outer: ',num)
    
outer()

def outer_fun():
    num = 6
    def inner_fun():
        nonlocal num  # to modify variable in enclosing scope, we need to use 'nonlocal' keyword
        num = 9
        print('inner num: ',num)
    print('outer num: ', num)
    inner_fun()
    print('outer num: ',num)

outer_fun()

'''
GLOBAL SCOPE: Variables defined at top level of script
'''

x = 'global x'
y = 'global y'

def getX():
    print(x)
    global y   # to modify global y variable  inside this function, we need to use global keyword
    y = 'local y'
    print(y)

print(y)    
getX()
print(y) 


# built-in scope: variables which aare built-in in python ,for example: min
print(min([12,10,1,67,4])) 