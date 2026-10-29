import csv

# this methods are preffered over reader and writer

with open('names.csv', 'r') as file:
    csv_reader = csv.DictReader(file)

    # prints in dict key and value pair
    # for line in csv_reader:
    #     print(line) # {'first_name': 'Aarav', 'last_name': 'Sharma', 'email': 'aarav.sharma@example.com'}

    # for line in csv_reader:
    #     print(line['email']) # aarav.sharma@example.com

    with open('new_file.csv', 'w') as new_file:
        field_names = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter='\t')

        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)
