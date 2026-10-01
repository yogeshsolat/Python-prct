# List
courses = ['Hindi', 'English', 'Maths', 'Science']
courses_2 = ['Chemistry', 'Arts']  
nums = [5, 2, 1, 4, 3]

# print(courses)            # prints whole list
# print(courses[0])         # prints element at 0th index
# print(len(courses))       # prints length of list
# print(courses[-1])        # prints last index value of the list
# print(courses[0:2])       # print elements of indexes from 0 to 1 (first argument is inclusive and second argument is exclusive)
# print(courses[:2])        # will print same as above
# print(courses[2:])        # will print values from 2nd index to last index

# courses.append('Physics') # adds value at the last of the list  
# courses.insert(0,'Arts')  # inserts/adds value at given index and dont overrides the other value
# print(courses)

# courses.insert(0,courses_2) # inserts the courses_2 whole list(not the individual elements) at the starting of courses list
# print(courses)              # looks like this [['Chemistry', 'Arts'], 'Hindi', 'English', 'Maths', 'Science']


# courses.extend(courses_2)   # adds the courses_2's individual elements at the ending of courses list
# print(courses)              # looks like this ['Hindi', 'English', 'Maths', 'Science', 'Chemistry', 'Arts']

# val = courses.pop()               # returns and removes the last value of list
# print(courses) 
# print(val)

# courses.reverse()           # reverse the list 
# print(courses)

# courses.sort()              # sort the list
# print(courses)

# courses.sort(reverse=True)  # sort list in reverse order 
# print(courses)  

# sorted_courses = sorted(courses) # returns the sorted version of list but does not tamper the original list
# print(courses)
# print(sorted_courses)

# print(min(nums))  # returns minimum number of list
# print(max(nums))  # returns maximum number of list
# print(sum(nums))  # returns sum of all numbers of list

# print(courses.index('Maths'))  # returns index of value if exists
# print(courses.index('Arts'))   # throws error because value not exists in list


# Boolean
# print('Arts' in courses)      # prints False because 'Arts' is not in the list
# print('Maths' in courses)     # prints True because 'Maths' is in the list


# loop over list, visit and print each item (only prints value)
# for item in courses:
#     print(item)

# prints each index and value of list    eg. (0, 'Hindi')
# for item in enumerate(courses):
#     print(item)

# this also prints index and value but gives better access to index and value vars eg. 0 Hindi
# for index,item in enumerate(courses):
#     print(index, item)

# it will print all value of list with index but index will start with 1
# earlier eg. 0 Hindi (index/count started from 0) now eg. 1 Hindi (index/count started from 1)
# for index,item in enumerate(courses, start=1):
#     print(index, item)

# List manipulation
# will create a string of comma separated values of list
# courses_str = ', '.join(courses)
# print(courses_str)                # output: Hindi, English, Maths, Science

# courses_str = ' - '.join(courses)
# print(courses_str)                # output: Hindi - English - Maths - Science


# turn back string to list
# courses_str = ' - '.join(courses)
# new_list = courses_str.split(' - ')
# print(new_list)                   # Back to the original list

