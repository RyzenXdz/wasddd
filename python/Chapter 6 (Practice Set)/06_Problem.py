# Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

Marks = int(input("Enter Your Marks In Test: "))

if(Marks >= 90 and Marks <= 100):
    print("Excellent")

elif(Marks >= 101):
    print("The Test Is Only Of 100 Marks.")

elif(Marks >= 80):
    print("The Grade Is A")

elif(Marks >= 70):
    print("Grade Is B")

elif(Marks >= 60):
    print("Grade Is C")

elif(Marks >= 50):
    print("Grade Is D")

else:
    print("Grade Is F")