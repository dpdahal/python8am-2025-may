# if,else,elif,nested if else

# x=8
# y=8
# if x==y:
#     print("yes")
# else:
#     print("no")
# print(x==y)

# WAP to enter any age and check if the person is eligible to vote or not.
# 18 > = eligible to vote

# age = int(input("Enter your age: "))
# if age>=18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# num =10
# if num%2==0:
#     print("Even")
# else:
#     print("Odd")

# a=5
# b=6
# c=7
# if a>b and a>c:
#     print("A")
# elif b>a and b>c:
#     print("B")
# else:
#     print("C")


# WAP to enter any alphabet and check if it is vowel or consonant.
# a,e,i,o,u are vowels
# WAP to enter five subject marks and calcualte totla per and grade

# nep =int(input("Enter Nepali marks: "))
# eng =int(input("Enter English marks: "))
# math =int(input("Enter Math marks: "))
# phy =int(input("Enter Physics marks: "))
# chem =int(input("Enter Chemistry marks: "))
# total = nep+eng+math+phy+chem
# per = total/5
# print("Total marks: ", total)
# print("Percentage: ", per)
# if per>80:
#     print("A+")
# elif per>60:
#     print("A")
# elif per>40:
#     print("B")

# else:
#     print("C")


# 1. Dell(Rs:20000) 2.HP(Rs:30000) 3. Lenovo(Rs:40000) 4. Apple(Rs:50000)
#  Enter your choice: 1
# Enter your quantity: 2
# Name

# WAP to enter any number and check it is divisible by 3 and 5 or not.
# nested if else statement

# name =input("Enter your name: ")

# if name=='admin':
#     age =input("Enter your age:")
#     print(name)
#     print(age)

# else:
#     print("Enter your name")

username=input("Enter your username: ")
password=input("Enter your password: ")

if username=='admin':
    if password=='admin002':
        print("Welcome to the system")
    else:
        print("Invalid password")
else:
    print("Invalid username")

# if username=='admin' and password=='admin002':
#     print("Welcome to the system")
# else:
#     print("Invalid username or password")
