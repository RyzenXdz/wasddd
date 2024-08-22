# Write a program to calculate the factorial of a given number using for loop.

# Get user input
number = int(input("Enter a number to calculate the factorial: "))

# Initialize factorial result
factorial = 1

# Calculate factorial using a for loop
for i in range(1, number + 1):
    factorial *= i

# Print the result
print("The factorial is:", factorial)
