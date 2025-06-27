my_msg='Prachi\'s message'

multiline_txt="""
hello
world
"""

#string methods

print(multiline_txt.upper())
print(multiline_txt.lower())

#to count occurance of a substring in a string
print(multiline_txt.count('hello')) 
print(multiline_txt.count('e'))

# to find index of a substring, return -1 if substring not found
print(multiline_txt.find('llo'))

#to get string length
print(len(my_msg))

# to access substring
print(multiline_txt[:4]) # prints from index 0 to 3
print(multiline_txt[1:]) # prints frrom index 1 till the end
print(multiline_txt[0])
print(multiline_txt[0:4]) #prints from index 0 to 3

# to replace a substring
comment='this is good'
print(comment.replace('this','it')) #replace returns a new string
print(comment)
comment = comment.replace('this','it')
print(comment)

# string concatination
greeting='hello'
name='prachi'

msg=greeting + " " + name
print(msg)

# using f-strings for string formatting and interpolation
msg2 = f'Good morning, {name.upper()}'
print(msg2)

#dir() method

# to get attributes and methods available on a variable
print(dir(msg2))

# to get list of all string methods and their details
print(dir(str))

#  to get detail about a specific string method
print(help(str.capitalize))