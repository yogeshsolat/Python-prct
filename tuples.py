# Tuples

"""
tuples are very similar to list but cannot modify them (list is mutable and tuples are not (immutable))
"""

# mutable example (how list works)
# list_1 = ['Maths', 'Science', 'History']
# list_2 =  list_1

# print(list_1)     # ['Maths', 'Science', 'History']
# print(list_2)     # ['Maths', 'Science', 'History']

# list_1[0] = 'Arts'

"""
    even though we changed list 1 but list 2 is also got changed because they share same referance 
    and thats how mutability changed the list2 as soon as we changed the list 1
"""

# print(list_1)     # ['Arts', 'Science', 'History']
# print(list_2)     # ['Arts', 'Science', 'History']


# Immutable example how tuple works
# tuple_1 = ('Maths', 'Science', 'History')
# tuple_2 = tuple_1

# print(tuple_1)      # ('Maths', 'Science', 'History')
# print(tuple_2)      # ('Maths', 'Science', 'History')

# tuple_1[0] = 'Arts' # TypeError: 'tuple' object does not support item assignment

"""
    tuple is immutable thats why we got type error because it does not support assignment
"""
# print(tuple_1)
# print(tuple_2)

"""
    because tuple is immutable, it doesnt have any large number of methods as of list
    so we cannot append or remove any thing here like list other wise its same like list
    you can loop over a tuple access elements etc etc
"""
