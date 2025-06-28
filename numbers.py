#  numbers in python - integer and float

num1 = 10
num2= 1.33
print(type(num1))
print(type(num2))
print(num1/num2)

# division in python return float, we can use floor division if integer result is required
res=4/2
print(res)

# we can convert float to integer using int() or round()
print(int(res)) 
print(round(num1/num2))

# floor division
print(num1//num2)

# abs(): to remove negative sign from a number
print(abs(-8))

# check for equality and non-equality
print( 3 != '3')
print(3 == 3)