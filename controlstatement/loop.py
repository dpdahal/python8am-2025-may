# what is loop?
# loop is a statement that repeats a block of code multiple times until a certain condition is met.
# In Python, there are two main types of loops: for loops and while loops nested loop.
# for: (collection) list, tuple, set, dictionary, string
# while: (condition) True, False

# students=['ram','hari','sita','gita']

# for name in students:
#     print(f"Hello: {name}")

# numbers=[1,2,3,4,5,6,7,8,9,10]
# for num in numbers:
#     if num%2==0:
#         print(num,end=" ")

# print(range(10))

# for i in range(1,10,2):
#     print(i, end=" ")

# data =[12,13,6000,9000,600,8900,15000,4000,3000,10000]

# >5000 < 10000

# enter number of times
# enter name?
# n=int(input("Enter number of times: "))
# students=[]
# for a in range(n):
#     name=input("Enter name: ")
#     students.append(name)


# for name in students:
#     print(f"Hello: {name}")




# i=1
# while i<=10:
#     print(i,end=" ")
#     i+=1

# data=['ram','sita','gita','hari']
# i=0
# while i<len(data):
#     print(data[i])
#     i+=1

# print(len(data))

# data=['ram','sita','gita','hari','ram','gita']
# new_list=[]
# for name in data:
#     if name not in new_list:
#         new_list.append(name)

# print(new_list)

# numbers=[
#     [12,14,15,16,89],
#     [98,87,65,43,21],
# ]


# def test():
    # """
    # this is test function
    # """
    #  this is test function
#     pass

# print(test.__doc__)

# students=[
#     {'name':'ram','address':'ktm'},
#     {'name':'sita','address':'ktm'},
#     {'name':'gita','address':'ktm'},
#     {'name':'hari','address':'ktm'}
# ]

# for user in students:
#     print(user['name'],user['address'])

# my name is ram and I live in ktm


# students=[
#     {'name':'ram','makrs':[67,87,56,76,90]},
#     {'name':'sita','makrs':[97,90,56,76,90]},
#     {'name':'gita','makrs':[34,87,52,12,87]},
#     {'name':'hari','makrs':[67,13,56,15,45]}
  
# ]
# for student in students:
#     total=0
#     for mark in student['makrs']:
#         total+=mark
#     per =total/5
#     grade =""
#     if per>=80:
#         grade="A"
#     elif per>=60:
#         grade="B"
#     elif per>=40:
#         grade="C"
#     elif per>=33:
#         grade="D"
#     else:
#         grade="F"

#     print(f"Name: {student['name']} Total: {total} Percentage: {per} Grade: {grade}")

# for x in range(1,5):
#     print(f"=============={x}==================")
#     for a in range(1,10):
#         print(a,end="")
#     print()


# total=0
# for x in range(1,51):
#     if x%2==0:
#         total+=1

# print(total)


# students=[
#     {'name':'ram','gender':'male','status':True},
#     {'name':'sophia','gender':'female','status':False},
#     {'name':'gopal','gender':'male','status':False},
#     {'name':'hari','gender':'male','status':False},
#     {'name':'sita','gender':'female','status':True},

# ]
# total_users =len(students)
# total_male=0
# total_female=0
# total_active_users=0
# total_inactive_users=0
# total_active_male=0
# total_active_female=0
# total_inactive_male=0
# total_inactive_female=0
# for student in students:
#     if student['gender']=='male':
#         total_male+=1
#     else:
#         total_female+=1

#     if student['status']==True:
#         total_active_users+=1
#         if student['gender']=='male':
#             total_active_male+=1
#         else:
#             total_active_female+=1
#     else:
#         total_inactive_users+=1
#         if student['gender']=='male':
#             total_inactive_male+=1
#         else:
#             total_inactive_female+=1


# print(f"Total Users: {total_users}")
# print(f"Total Active Users: {total_active_users}")
# print(f"Total Inactive Users: {total_inactive_users}")
# print(f"Total Male Users: {total_male}")
# print(f"Total Female Users: {total_female}")
# print(f"Total Active Male Users: {total_active_male}")
# print(f"Total Inactive Male Users: {total_inactive_male}")
# print(f"Total Active Female Users: {total_active_female}")
# print(f"Total Inactive Female Users: {total_inactive_female}")


category=[
    {'cid':1,'name':'laptop'},
    {'cid':2,'name':'mobile'},
    {'cid':3,'name':'tv'},
]


products=[
    {'pid':1,'cid':1,'name':'dell','price':50000,'qty':10},
    {'pid':2,'cid':1,'name':'mac','price':90000,'qty':8},
    {'pid':3,'cid':2,'name':'mi','price':20000,'qty':60},
    {'pid':4,'cid':3,'name':'sony','price':15000,'qty':30},

]

# category: laptop
#           dell
#           mac
# category: mobile
#           mi


# continue
# break

# patterns

# 1
# 12
# 123
# 1234
# 12345

# *
# **
# ***
# ****
# *****

# 12345
# 1234
# 123
# 12
# 1


# enter number 
#  1,2,3,4,1,2


# numbers=[
#     [10,20,30,44,56],
#     [54,2,3,4,50],
#     [12,13,14,15,16]
# ]

# array=[]


# enter number of students
# name,gender,age
# old


# break
# for x in range(1,11):
#     if x==5:
#         break
#     print(x)
# continue

# for x in range(1,11):
#     if x==5 or x==7:
#         continue
#     print(x,end=" ")