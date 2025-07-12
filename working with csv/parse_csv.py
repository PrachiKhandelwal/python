import csv
import os

currentFilePath = os.path.abspath(__file__)
currentDirectory =  os.path.dirname(currentFilePath)

csvFilePath = os.path.join(currentDirectory,'fake_users.csv')

# reading csv file
with open(csvFilePath,'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    # for line in csv_reader:
    #     print(line)
    #     print(line[2])

# copy csv file contents into another file
copyFilePath=os.path.join(currentDirectory, 'copy.csv')

with open(csvFilePath,'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    with open(copyFilePath,'w',newline='') as csv_file_copy:
        csv_writer=csv.writer(csv_file_copy,delimiter='\t')
        for line in csv_reader:
            csv_writer.writerow(line)

# reading using dictionary reader
with open(copyFilePath,'r') as copy_file:
    csv_reader = csv.DictReader(copy_file,delimiter='\t')
    for line in csv_reader:
        print(line["first_name"])

# writing using dictionary writer
with open(csvFilePath,'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    with open(copyFilePath,'w') as copy_file:
        fieldNames=["first_name","last_name"]
        csv_writer=csv.DictWriter(copy_file,delimiter=' ',fieldnames=fieldNames)
        csv_writer.writeheader()
        for line in csv_reader:
            del line["email_id"]
            csv_writer.writerow(line)