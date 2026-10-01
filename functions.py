"""
    Functions allows us to reuse the code without repeating ourselves
"""

# void function
def fun():
    print("hello function")

fun()

# function which returns value 
def ret_fun():
    return "ye le bhai string"

print(ret_fun())
print(ret_fun().upper())

# function which has arguments
def arg_fun(arg):
    return f"heres your {arg} in return"

print(arg_fun("demo"))


# funtion with default arg value
def def_arg_val(arg = "iiii", arg1 = 'you'):
    return f"heres your 1st arg: {arg}, and 2nd arg: {arg1}"

print(def_arg_val("ohayo"))
print(def_arg_val("ohayo", "gozaimasu"))
print(def_arg_val("ohayo", arg1 = "senpai"))

# below declartion will give you error because python expects non default values/ args should come/declare first
# def def_arg_val(arg = "iiii", arg1):
#     return f"heres your 1st arg: {arg}, and 2nd arg: {arg1}"


# when we dont know how many arguments does our function need then we go to this approach 
# *args for positional arguments
# **kwargs for keyword arguments

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', 'Arts', name= 'john', age = '24' )



courses = ['Math', 'Science', 'Arts']
info = {'name': 'Roy', 'age': '22'}

student_info(courses, info) # wont un pack the values
student_info(*courses, **info) # will un pack the values