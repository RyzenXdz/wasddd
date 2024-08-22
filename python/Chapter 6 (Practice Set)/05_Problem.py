# Write a program which finds out whether a given name is present in a list or not

let_list = ["Hey", "Hello", "I", "I am", "Harry", "How"]

let_int = input("Enter Any English Word: ")

if(let_int in let_list):
    print("These Are Our Personal Private Words.")

else:
    print("The Word You Have Given Is", "{", let_int, "}")