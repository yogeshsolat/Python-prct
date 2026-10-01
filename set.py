"""
    sets are values who has no order and has no duplicates
    its used to test whether a value is part of a set, set does this lot more efficiently than tuple and list
"""

# courses = {'Maths', 'Science', 'History', 'Geography'}
# print(courses)   # does not maintain insertion order : {'History', 'Science', 'Geography', 'Maths'} ( order will change with each execution)

# courses = {'Maths', 'Science', 'Science', 'History', 'Geography', 'Maths'}
# print(courses)    # removed duplicates : {'Geography', 'Science', 'Maths', 'History'}

# courses = {'Maths', 'Science', 'History', 'Geography'}
# print('Maths' in courses) # prints : True 
# we can do this with tuples and list too but sets are optimized for this 

cs_courses = {'Maths', 'Science', 'History', 'Geography'}
arts_courses = {'Maths', 'Science', 'Arts', 'Design'}

# returns the values that are common in both sets
print(cs_courses.intersection(arts_courses)) # {'Science', 'Maths'}

# returns the values which are in cs_courses but not in arts_courses
print(cs_courses.difference(arts_courses)) # {'Geography', 'History'}

# returns all of the values of both sets
print(cs_courses.union(arts_courses)) # {'Arts', 'Design', 'Science', 'Geography', 'History', 'Maths'}


