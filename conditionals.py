# conditionals:
# Equal:              ==
# Not Equal:          !=
# Greater than:       >
# less than:          <
# Greater or Equal:   >=
# Less or Equal:      <=
# Object Entity:      is


# if True:
#     print('its true!')

# if False:
#     print('it wont print')

language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is JavaScript')
elif language == 'Java':
    print('Language is JavaScript')
else:
    print('No match')


"""
    python doesnt have switch case statements !!!!!
"""


a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)               # True :  compares values inside of list

print(id(a))
print(id(b))
print(a is b)               # False : because both are different objects and has different ids; dont rely on values( checks is both object are same )



# True scenario for 'is' conditional: 
# a = [1, 2, 3]
# b = a

# print(id(a))
# print(id(b))

# print(a is b)               # True: both are same objects and has same ids



# False values:
    # False
    # None
    # zero of any numeric type
    # Any empty seequence. eg,  '', (), [].
    # Any empty Mapping. eg,  {}

condition = {}

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')