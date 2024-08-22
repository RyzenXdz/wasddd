# Write a program to find whether a given number is prime or not.

bill = int(input("Enter Your Favourite Number: "))

odd_prime = [1, 9, 15, 21, 25, 27, 33, 35, 39, 45, 49, 51, 55, 57, 63, 65, 69, 75, 77, 81, 85, 87, 91, 93, 95, 99]

for i in range(1, 3):
  let = bill % i
  if (let == 0 or bill == odd_prime):
    print("The Number Is Not Prime")

  elif(bill == odd_prime):
    print("The Number's Are Not Prime")

  elif(bill == 2):
    print("Number Is The Prime")