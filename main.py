# print("hello world")
# x=7
# y=6
# print(x/y)

# #Arithmetic operators

# x=10
# y=90
# print(x+y)
# print(x-y)
# print(x/y)
# print(x*y)

# #Realtional/camparison operators

# a = 50
# b = 30

# print(a == b)  #false
# print(a != b)  #true
# print(a >= b)  # true
# print(a > b)   #true
# print(a <= b)  #false
# print(a < b)   #false

#  # Assignment operators

# num = 10
# num = num + 10
# num += 10
# print("num :",num)

# #logical operators
# a = 50
# b = 30

# print(not False)
# print(not (a > b))

# val1 = True
# val2 = True
# print("AND operator:", val1 and val2)

# # type conversion

# a = 2
# b = 4.25

# sum = a + b 
# print(sum)

#input

# name = input("enter your name :")
# print("welcome", name)
# age = input("enter age:")

# Assignment 1

# diameter = int(input(" enter the diatmeter of the circle :"))
# radius = diameter / 2
# area = 3.14 * (radius ** 2)
# print("Radius of the circle is :", radius)
# print("area of a circle :", area) 

# marks = 98

# if(marks >= 90):
#     print("your grade is A+")

# elif(marks <= 75):
#     print("your grade is B")

# Age = 15

# if("Age>=18"):
#     print("you are eliglible to vote")

# else:
#     print("your are not eligible to vote")


#assignment

# num = int(input("enter a number :"))

# if(num>0):
#     print("positive")
# elif(num==0):
#     print("zero")
# else:
#     print("negative")

#list


# my_list=["apple","banana","cherry"]

# print(my_list[1])

# print(my_list[-1])

my_list=["apple","banana","cherry","sjc","bdsku","vbhsvc"]

print(my_list[2:5])

print(my_list[-2:5])
print(my_list[-5:-2])
print(my_list[-4:0])
print(my_list[-4:])

my_list=["apple","banana","cherry","sjc","bdsju","vbhsu"]
my_list[1]="mango"
print(my_list)

#tuples
mytuple= (25, 64, 47)
studentTuple= ("riya", "mahi", "sonali",)

# print(studentTuple[2])

#empty tuple

emptyTuple= ()
singleTuple= (1,)
print(type(emptyTuple))
print(type(studentTuple))



# x="what"
# y="is"
# t="python"
# print(x,y,t)

# def my_func():
#     global x
#     x="good"
# my_func()
# print("python is " + x)
# #fgg7uj
# my_list=["apple","banana", 1 ,3 ,5 ,7]

# my_list[2]="abc"

# print(my_list)


# my_list=["apple","banana",1,3,5,7]

# my_list[2:5]=["abc"]

# print(my_list)


# my_list=[1,2,4,5,6]

# my_list.insert(2,3)

# print(my_list)

# list1=[1,3,5,6]
# list2=["mango","yaghs","lais"]
# list1.insert(1,2)
# list1.insert(3,4)
# print(list1)
# list1.append(list2)
# print(list1)
# list1.extend(list2)
# print(list1)


# #clear
# list1=[1,5,3,8]
# list.clear(list1)
# print(list1)

# list1=[]
# list1.append(1)
# print(list1)

# list1[0]="hello"
# print(list1)


# #looplists

# list1=[1,2,3,4,5,6]
# for x in list1:
#     print(x)

# list1=[1,2,3,4,4,4,4,5,6]
# for x in list1:
#     print(x)

# #sort 
# list=[1,2,3,1,8]

# list.sort()
# print(list)

# list=[2,5,1,4,6]
# list.sort(reverse=True)
# print(list)

# text="hello"
# print(text.upper())

# text="SONI"
# print(text.lower())

# print(text.strip())
# print(text.replace("hello","world"))
# print(text.split())


# #Formatstring

# x="bob"
# y=37

# print(f"my name is {x} and my age is {y}")

# # operation
# x=5
# x+=3

# print(x)


# y=7
# y*=8
# print(y)

# z=2
# z/=84
# print(z)

# a=67
# a%=36
# print(a)

# # camparison operator:

# x=29
# y=7
# print(x>y)#true
# print(x==y)#false
# print(x!=y)
# print(x>=y)
# # print(x<=y)

# # logical operators

# a=5
# print(a>5 and a<10)#true #(and)
# print(not(a>3))#false  #(not)

# # Identity operators

# x=[1,2,3]
# y=x
# z=[1,2,3]
# print(x is y)  #true
# print(x is z)  #false
# print(y)
# print(z is y)
# print(x is not y)

# # python Tuples
# # python Sets
# # creating sets
# colors={"red","green","blue"}
# for x in colors:
#     print(x)

# #Adding Elements

# colors.add("yellow")
# print(colors)

# #REMOVING Elements

# colors.remove("green")
# print(colors)

# #Python dictionaries

# students={
#     "name":"soni",
#     "age":30,
#     "grade":"A"
# }
# print(students)

# #if else 

# age=42

# if age>=18:
#     print("you are adult")
# else:
#     print("you are not adult")
#     age=26
# if age<=18:
#     print("you are adult")
# else:
#     print("you are not adult")

# #If..elif..else
#     marks=38
# if marks>=85:
#     print("Grade:A+")
# elif marks>=70:
#     print("Grade:A")
# elif marks>=60:
#     print("Grade:B")
# else:
#     print("Grade:C")

#     #if else
# age=16
# if age>18:
#     print("you are adult")
# elif age==18:
#     print("you are teen")
# elif age==17:
#     print("you are 17")
# elif age==16:
#     print("you are 16")
# else:
#     print("you are not adult")

#     #Nested if 
#     x=15
#     if x>10:
#         print("x is greater then 10")
#     if x>20:
#         print("x is greater then 20")
#     else:
#         print("x is not greater then 20")


#     x=10
#     if x>20:
#         print("x is greater then 20")
#     if x==10:
#         print("x is equal to 10")
#     else:
#         print ("x is not greater then 10")





# x=5
# if x>2:
#     print("this is an odd number")
# else:
#     print("this is not odd number")


# x=15

# if x%2==0:
#     print("even")
# else:
#     print("odd")


#     fruits="apple","banana","pineapple"
#     for x in fruits:
#         print(x)

# # range for loops

#         x=[0,1,2,3,4,5]
#         for i in range(5):
#             print(i)

# # range(start,stop,step)
# # for i in range(1,10,2):
# #     print(i)

# # for i in range(1,4):
# #     for j in range(1,3):
# #         print(f"i={i},j={j}")

# # for i in range(1,6):
# #     print(i)
# # else:
# #     print()

# # i=5
# # while i <=20:
# #     print(i)
# #     i +=1

# # i=1
# # while i<=10:
# #     print(3*i)
# #     i += 1

# # def greet():

# #     print("Hello,python!")

# # greet() #calling the function

# # #Function 

# # def greet(name):
# #     print(f"hello,{name}")

# # greet("alice")
# # greet("bob")

# # function with return value

# def add(a,b):
#     return a+b
# result=add(5,3)
# print(result)

# x=12
# def my_func():
#     y=5
#     print(x,y)
# my_func()

# print(x)

# class car:
#     def __init__(self,brand,color):
#          self.brand=brand
#          self.color=color

#     def drive(self):
#         print(f'{self.color} {self.brand} is driving')

# # #object
# # car1=car("bmw","black")

# # car1.drive()
    
# #     python Arrays 



# # create an array of integers

# # number=array
# # .array[1,2,3,4,5]
# # print(number)

# from numpy import random  # type: ignore

# x=random.randint(100)
# print(x)

# x= random.rand(1,25)
# print(x)

# x=random.rand(1,90)
# print(x)

# import random

# x=random.random()
# print(x)

# [23]
# [1,2,3,4,5,]

# [[1,2,3],
#  [4,5,6]]

# [[[1,2,3],
#  [4,5,6]]
# [[7,8,9],
#  [10,11,12]]]

# x=random.randint(100,size=(5))
# print(x)

# x=random.randint(100,size=(3,5))
# print(x)


# x=random.randint(100,size=(5,6))
# print(x)

# x=random.randint(100,size=(2,3,5))
# print(x)

# x=random.randint(100,size=(2,6,7,3))
# print(x)

# from numpy import random

# # x=random.choice([2,5,6],size=(5))
# # print(x)

# # x=random.choice([4,5,6],size=(5,2,3))
# # print(x)

# #pandas

# #creating a series 

# # import pandas as pd 

# # data=[10,20,30,40]
# # s=pd.Series(data)
# # print(s)

# #DATAFRAME

# import pandas as pd

# data={
#     "Name":["alice","bob"],
#     "age":[26,73],
#     "city":["delhi","mumbai"]
# }
# df=pd.DataFrame(data)
# print(df)

# import numpy as np

# arr=np.array([1,2,3,4,5])
# s=pd.Series(arr)
# print(s)

# #From a dictionary

# Data={"main":90,"science":58,"english":75}
# s=pd.Series(Data)
# print(s)