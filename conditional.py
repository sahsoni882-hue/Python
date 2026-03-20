# age = int(input("Enter your age: "))

# if age >= 18:

#     print("You are eligible to vote.")

# else:

#     print("You are not eligible to vote.")

# color = input("Enter your favorite color: ")

# if color == "red":

#     print("Your favorite color is red.")

# elif color == "blue":
#     print("Your favorite color is not red.")
# elif color == "green":
#     print("Your favorite color is green.")
# else:
#     print("Your favorite color is not red, blue, or green.")

# no = [1,-3, 2, -4, 5, 9,10, -32,-45]
# positive_num_count=0
# for number in no:
#     if number > 0:
#         positive_num_count += 1

# print("final count of positive numbers is:", positive_num_count)

# while loop 

# i = int(input("Enter a value of i: "))

# while (i <= 32):

#     i= int(input("enter the value of i: "))

#     print(i)


# if(i==32):

#     print(input("enter the  smaller value of i: "))

# else:

#     print("Done with the loop")



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

for i in range(1, 11):
    if i == 6:
        continue
    print(f"9 x {i} = {9 * i}")



# for i in range(1, 11):
#     if i == 5:
#         break
#     print(f"9 x {i} = {9 * i}")

#  while loop 

i = int(input("Enter a value of i: "))

while (i <= 32):

    i= int(input("enter the value of i: "))

    print(i)


if(i==32):

    print(input("enter the  smaller value of i: "))

else:

    print("Done with the loop")




