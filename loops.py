numbers=[1,2,3,4,5]

for num in numbers:
    if(num == 3):
        print('Found 3')
        break
    print(num)

for num in numbers:
    if(num % 2 == 0):
        continue
    print(num)

for num in numbers:
    for letter in 'prachi':
        print(f'{num} - {letter}')

# print numbers from 1 to 10
for i in range(1,11):
    print(i)

# while loop

x=0

while x < 10:
    if(x == 5):
        break
    print('x: ',x)
    x+=1