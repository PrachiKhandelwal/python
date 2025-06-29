# set is unordered collection of unique items

subjects={'history','math','civics','chemistry','math'}

print(subjects)

print('math' in subjects)

# to get common values in two sets
subjects_2={'history','english','civics'}
print(subjects.intersection(subjects_2))

# to get values present in subjects_2 but not in subjects
print(subjects_2.difference(subjects))

# to get all values present in both sets
print(subjects.union(subjects_2))

#  to create an empty set
empty_set=set()
print(empty_set)
empty_set.add(3)
print(empty_set)