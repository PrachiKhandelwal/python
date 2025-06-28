tech=['react','node','python']

print(tech[- 1])

print(tech[0:2])

# accessing an index that does not exist results in "list index out of range" error
# print(tech[10])

# to get length of list
print(len(tech)) 

# to add new element to end of list
tech.append('fastapi')
print(tech)

# to add new element at specific position
tech.insert(2,'Flask')
print(tech)

# to add multiple values to list, we use  extend

tech2=['next.js']
tech.extend(tech2)
print(tech)

# to delete specific element from list
tech.remove('react')
print(tech)

#to remove last element of a list
val=tech.pop()
print(f'{tech}, {val}') 

# reverse a list
tech.reverse()
print(tech)

#sort a list in ascending order (case  insensitive sort using key)
#sort modifies original list
tech.sort(key=str.lower)
print(tech)
nums=[3,7,11,1,45,7,1]
nums.sort(reverse=True)
print(nums)

#sort in descending order
tech.sort(reverse=True)
print(tech)

# if we want to sort a lissst but not modify the original list, we can use sorted() method
print(nums)
sortedList=sorted(nums)
print(sortedList)
print(nums)

# to get min, max value and sum of list
print(min(nums))
print(max(nums))
print(sum(nums))

# to get first index of an element in a list
print(nums.index(1))

# to get if an element exists in a list
if 17 in nums:
    print('17 is present')
else:
    print('17 not found')

print('ml' in tech)

for technology in tech:
    print(technology)

for index,num in enumerate(nums):
    print(f'value on index {index} is {num}')

tech_str=', '.join(tech)
print(tech_str)
retrieved_tech=tech_str.split(', ')
print(retrieved_tech)

subjects_1=['history','math','civics','chemistry']
subjects_2=subjects_1

subjects_1[0]='physics' #modifies both subjects_1 as well as subjects_2 value
print(f'{subjects_1}, {subjects_2}')