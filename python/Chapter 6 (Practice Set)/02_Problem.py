# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

Marks_1 = int(input("Enter Your Marks In Math: "))

Marks_2 = int(input("Enter Your Marks In Science: "))

Marks_3 = int(input("Enter Your Marks In Computer: "))

if (Marks_1 and Marks_2 and Marks_3 > 33):
   print("You Are Passed, Marks Total:", Marks_1 + Marks_2 + Marks_3)

elif (Marks_1 and Marks_2 and Marks_3 < 33):
      
   print("You Are Failed, Marks Total:", Marks_1 + Marks_2 + Marks_3)