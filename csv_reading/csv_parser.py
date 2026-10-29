import csv

with open('names.csv', 'r') as file:
    data = csv.reader(file)

    # next(data) #excludes/skips headings/1st row

    # prints all data and its fields
    # for line in data:
    #     print(line)

    # prints only emails
    # for line in data:
    #     print(line[2])

    with open('new_file.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter= '\t') # will give space tab between values instead of comma

        for line in data:
            csv_writer.writerow(line)

    # to read this newly created csv by us we need to specify the delimiter as tab 
    # when we need to create a csv.reader() variable otherwise it wont read correctly

with open('new_file.csv', 'r') as newer_file:
    data = csv.reader(newer_file, delimiter='\t')

    for line in data:
        print(line)