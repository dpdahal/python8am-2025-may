# what is function?
# function is a block of code that only runs when it is called
# there are two types of functions: 
# 1. built-in functions -> print(), len(), type(), etc.
# 2. user-defined functions -> functions that you create yourself

#  def function name
# rule for creating function name:
# 1. function name should be descriptive and meaningful
#  2. function name should be in lowercase
# 3. function name should not start with a number
# 4. function name should not contain spaces
# 5. function name should not be a keyword

# def hello():
#     print("Hello Python!")


# hello()
# hello()


# def hello(name):
#     print("Hello",name,"!")

# hello("python")
# hello("Dotnet")

#  WAP to enter three numbe and print their sum

# def add(x,y,z):
#     pass

# optional parameter

# def hello(name='java'):
#     print("Hello",name,"!")

# hello('php')

# def user(name,address,age=0):
#     print(name)
#     print(age)

# user('ram')

# def users(names):
#     print(names)


# users(['ram','gita','sita'])

# array argument
# keyword argument

# def users(*args,**kwargs):
#     print(args)
#     print(kwargs)


# users('ram','gita','sita',name='sophia',age=30,city='kathmandu')

# print("hello","python","test")

# def add(x,y):
#     total= x+y
#     return total

# print(add(4,5))



# def add(x,y):
#     sm= x+y
#     sub= x-y
#     return sm
#     return sub

# sm = add(5,7)
# print(sm)

# sm = add
# print(sm(6,7))

# function scope

# # local sope
# def message():
#     a=60
#     print(a)

# message()
# print(a)


# global sope
# a=60
# def message():
#     print(a)

# message()
# print(a)

# a=60
# def message():
#     global a
#     a=50+a
#     print(a)

# message()
# print(a)


# def college():
#     def student():
#         return "I am a student"
#     return student

# a=college()
# print(a())

# import math
# print(dir(math))


# match


# lambda function

# def total(x,y):
#     return x+y

# print(total(5,6))

# total =lambda x,y: x+y
# print(total(5,6))

# 5-> 120
# 5-1: 4*5 =20
# 4-1: 3*20 =60
# 3-1: 2*60 =120

# def fac(n):
#     if n==1:
#         return 1
#     else:
#         return n*fac(n-1)
    
# print(fac(5))


# def hello():
#     print("Hello Python!")
#     hello()
    
# hello()

# WAP to enter any number and repeat it 5 times

def fac(n):
    if n==0:
        return 
    else:
        print("Hello Python!")
        fac(n-1)
    
fac(5)