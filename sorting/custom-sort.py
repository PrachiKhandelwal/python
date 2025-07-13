from operator  import itemgetter

# sort the tuple based on the absolute value of the items
tup = (12, 6, 8, 10, 78, 2,-11)
s_tup  = sorted(tup,key=abs)
print(s_tup)

# sort list of employee dictionary
employees=[{'name':'riya','os':'linux','salary':100000},{'name':'rashi','os':'windows','salary':120000},{'name':'sid','os':'windows','salary':90000},{'name':'shreya','os':'windows','salary':90000}]

def e_sort_by_name(emp):
    return emp['name']

# to sort employees list based on employee name
s_employees = sorted(employees,key=e_sort_by_name)
print(s_employees)

# to sort employees list based on salary from highest to lowest
def sort_emp_by_salary(emp):
    return emp['salary']

s_employees_by_salary = sorted(employees, key=sort_emp_by_salary,reverse=True)
print(s_employees_by_salary)

# to sort employees list based on length of name
s_employees_by_name_length = sorted(employees, key=lambda emp: len(emp['name']))
print(s_employees_by_name_length)

# we can also use itemgetter() method to sort using any item value
s_employees_by_os = sorted(employees,key=itemgetter('os','name')) # sort by os, followed by name 
print(s_employees_by_os)