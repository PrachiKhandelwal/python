li = [12, 6, 8, 10, 78, 2]

# sorted returns a new sorted list
# sorted works  for any type of iterable including list
li_sorted = sorted(li)
print(li,li_sorted)

# sorting tuple in descending order using sorted()
tup = (12, 6, 8, 10, 78, 2,-11)
s_tup = sorted(tup,reverse=True)
print(s_tup)

# getting sorted keys of dictionary using sorted()
di = {'name':'prachi','profession':'software engineer','os':'windows'}
s_di = sorted(di)
print(s_di)

# list.sort() method sorts the original list and return None
# sort() method works only for lists
li.sort(reverse=True)  # reverse=True sorts in descending order
print(li)

