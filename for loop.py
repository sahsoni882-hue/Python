# rows = 6
# for i in range (rows):
#     #print spaces
#     for j in range (rows - i - 1):
#         print(" ", end="")
#     #print stars
#     for k in range (2 * i + 1):
#         print("*", end="")
#     print()

# # inverted pyramid
# n = int(input("Enter the number of rows: "))
# for i in range(n, 0, -1):
#     # print spaces
#     for j in range(n - i):
#         print(" ", end="")
#     # print stars
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()

#write the table of 9 but skip the 5 itertion

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(f"9 x {i} = {9 * i}")

    # if i == 6:
    #     continue
    # print(f"9 x {i} = {9 * i}")



# for i in range(1, 11):
#     if i == 5:
#         break
#     print(f"9 x {i} = {9 * i}")

#  while loop 

# i = int(input("Enter a value of i: "))

# if(i < 38):

#     i= int(input("enter the value of i: "))

#     print(i)


# if(i>32):

#     print(input("enter the  smaller value of i: "))

# else:

#     print("Done with the loop")

# def multiply(a1, a2):

#     print(a1 * a2)

#     return(a1*a2)

# print(multiply(5, 6))

# def user (name):

#     return(name)

# print(user(name = input("Enter your name: ")))

# def print_name(name):
#     print("hello," + name + "!")

# user_name = input("Enter your name: ")
# print_name(user_name)


# def user (age):
#     return(age)

# print(user(age = int(input("Enter your age: "))))

# list [1, 2, 3, 4, 5]
# tuple (1, 2, 3, 4, 5)
# set {1, 2, 3, 4, 5}
# dict {"name": "John", "age": 30, "city": "New York"}


a = {"3": "5", "age": 30, "city": "delhi"}
print(a)

b = [12, 46, 58, 8, 66]
print(b)

c = (19, 24, 32, 45, 55)
print(c)