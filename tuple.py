# tuples are immutable lists

subjects_1=('history','math','civics','chemistry')
subjects_2=subjects_1

subjects_1[0]='physics' 
print(f'{subjects_1}, {subjects_2}')