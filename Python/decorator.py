# def decor_function(function):
#     def product():
#         print("This is a good product")
#         function()
#     return product()

# @decor_function
# def IIT():
#     print("IIT is a good institute")

# iterator 

# list = [34,90,45,32,12,54,32]

# x = iter(list)

# print(next(x))
# print(next(x))

# # generator

# def add (a,b):
#     yield a

#     yield b

# print(add(2,3))
# print(type(next))

## swapping of two numbers

# a = 90
# b = 100

# print("The value of a is : ",a)
# print("The value of b is : ",b)

# a , b = b , a

# print("The new value of a is : ",a)
# print("The new value of b is : ",b)

# def fun  (x,y):
#     z = x,y
#     print (z)

# fun(2,3)
# fun(90,'man')
# fun('man','woman')


def fun  (*x):
    for i in x:
        print (i)

fun(2,3)
fun(90,'man')
fun('man','woman')
