import os

# print(dir(os)) # this will show all the attributes and methods in given module/library that we can use

# print(os.getcwd()) # prints the current working directory

# os.chdir('users/etc') # shifts current file to a provided directory

# print(os.listdir()) # shows all files and directories of given path, if path not provided it shows for current file path

# os.mkdir('/demo')     # will create demo dir

# os.mkdir('/users/temp') # will create /temp dir inside /users dir, but if users dir is not exist then it will give error

# os.makedirs('/users/temp') # it will create users as well as temps dirs in one shot , it was not possible with os.mkdir() cmd

# os.rmdir('/users/temp')  # this will not remove intermediate directories it will delete only last i.e /temp

# os.removedirs('/users/temp') # it will remove all intermediate dirs also i.e /users and /temp

# os.rename('test.txt', 'demo.txt') # rename the file or folder test.txt ---> demo.txt

# os.stat('demo.txt') # gives info of given file

# os.stat('demo.txt').st_size  # will give size of file in bytes

# os.stat('demo.txt').st_mtime  # will give modified file time stamp

#--------------------------------------------------------------------------------

# from datetime import datetime

# mod_time = os.stat('demo.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))  # converts timestamp to readable date time


# if we want to see entire directory tree and files withing desktop 
# os.walk() # its a generator that yeilds a tuple of 3 values as its walking the dir tree
            # each dir it sees it yeilds 
                # -- dir path
                # -- directories within the path
                # -- files within the path

# can use below syntax too for walk

# for dir_path, dir_names, file_names in os.walk('/users/demo'):
#     print(dir_path)
#     print(dir_names)
#     print(file_names)

os.environ # will print/get all environment variables
os.environ.get('HOME') # will get only HOME named environment variable

os.path.join('/path/a','path/b')  # it joins 2 paths together, safe than concatination (it will manage slashesh all by itself)

os.path.basename('/temp/demo.txt') # prints demo.txt
os.path.dirname('/temp/demo.txt') # prints /temp
print(os.path.split('/temp/demo.txt')) # prints both firstt will print dir names , then file names ('/temp', 'demo.txt')
print(os.path.splitext('/temp/demo.txt')) # splits the file and extention use ful for just to get file name or file extention
                                        # ('/temp/demo', '.txt')