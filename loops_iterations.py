nums = [1, 2, 3, 4, 5]

# break     --->  breaks the whole loop 

# it will print 1 to 2 and on 3rd value it will print found and will break and exit the loop

# for num in nums:
#     if num == 3:
#         print('found')
#         break
#     print(num)


# continue  ---> skip the current and continue to next iteration

# will print all numbers except 3 because it has skipped that iteration

# for num in nums:
#     if num == 3:
#         print('found')
#         continue
#     print(num)

# inner loops

# for each number it will loop through every charcater

# for num in nums:
#     for letter in 'abc':
#         print(num , letter)


# range  ----> specify the range of iterations (if you want to run loop 10 times set range to 10)

# will print 0 - 9
# for i in range(10):
#     print(i)

# will print 1 - 10
# for i in range(1, 11):
#     print(i)


# while loop

x = 0

# while x < 10:
#     print(x)
#     x += 1


# will print 0 - 4

# while x < 10:
#     if(x == 5):
#         break
#     print(x)
#     x += 1