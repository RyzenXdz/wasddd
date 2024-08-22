# Write a program to find whether a given username contains less than 10 characters or not.

character = input("Enter Your Username: ")

let = len(character)

if(let >= 10):
    print("Username Is Too Long More than 10 characters")

else:
    print("Username Registered less than 10 characters")