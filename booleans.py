
# Booleans
# and
# or
# not           # inverts values (if true then it will become false and vice - versa)

user = 'Admin'
logged_in = False

# if block will execute if both values are true
# if user == 'Admin' and logged_in:
#     print('Admin page')
# else:
#     print('bad credentials')


# if block will execute if either values are true
# if user == 'Admin' or logged_in:
#     print('Admin page')
# else:
#     print('bad credentials')

if not logged_in:
    print('Please login')
else:
    print('welcome')