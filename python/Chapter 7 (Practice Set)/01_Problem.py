# Write a program to print multiplication table of a given number using for loop.

n = int(input("Enter Your Favourite Number: "))

for i in range (1, 11):
   print(f"{n} X {i}: ", n * i)