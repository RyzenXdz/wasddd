# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

let = input("Enter Your Name: ")

l = []

if("s" in let):
    l.append(let)

    print("You are Special: ",l)

else:
    print("You are Average And Normal")