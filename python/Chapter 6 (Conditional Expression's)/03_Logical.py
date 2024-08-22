# Logical operators in Python (and, or, not) let you check if two things are both true



# In Python:

# and: True if both conditions are true.

# or: True if at least one condition is true.

# not: Inverts the condition

# "here is the example of Number Gussing game"

secret_number = 7  # The secret number to guess

guess = int(input("Guess the number (between 1 and 10): "))

if guess == secret_number:
    print("Congratulations! You guessed the number.")
elif not (1 <= guess <= 10):
    print("Out of range! Guess a number between 1 and 10.")
else:
    print("Incorrect guess. Try again!")


