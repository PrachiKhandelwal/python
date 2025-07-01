import my_module as mm
from dummy import random_str as SAMPLE_STR

import sys
import random
import datetime

courses = ['math','english','history','chemistry']

index = mm.find_index('history',courses)
print(index)

print('sample value: ',SAMPLE_STR)

print(sys.path)

print(random.choice(courses))

today = datetime.date.today()

print(today)