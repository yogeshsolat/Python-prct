# student = {'name': 'john doe', 'age': 23, 'courses': ['Maths', 'Science', 'History']}
# print(student['name'])

# student = { 1: 'john doe', 'age': 23, 'courses': ['Maths', 'Science', 'History']}
# print(student[1])


student = {'name': 'john doe', 'age': 23, 'courses': ['Maths', 'Science', 'History']}

# print(student['phone'])       # will give key error because key does not exist
# print(student.get('name'))
# print(student.get('phone'))   # will return None instead of error if key not found
# print(student.get('phone', 'Not found'))      # will print 'Not Found' if key not found

# student['phone'] = '78787232'     # updates the value or creates a key and value if key not exists
# student['name'] = 'roy'
# print(student.get('phone', 'Not Found'))

# add or update multiple values in shot
# student.update({'name': 'john snow', 'height': 6.5})
# print(student)


# delete key
# del student['age']
# print(student)

# remove and return the value 
# age = student.pop('age')
# print(age)
# print(student)

# length of dict (number of keys)
# print(len(student))

# print all keys of dict
# print(student.keys())         # dict_keys(['name', 'age', 'courses'])

# print all values of dict
# print(student.values())       # dict_values(['john doe', 23, ['Maths', 'Science', 'History']])

# print all key value pairs of dict
# print(student.items())        # dict_items([('name', 'john doe'), ('age', 23), ('courses', ['Maths', 'Science', 'History'])])


# iterate all keys
for key in student:
    print(key)

# iterate each key value pair
for key, value in student.items():
    print(key, value)