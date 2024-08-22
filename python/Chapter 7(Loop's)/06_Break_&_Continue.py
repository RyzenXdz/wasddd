""" Break In Python """

# Break Is Use To Exit The Loop

for i in range (33):
    print(i) # Will Print Numbers 0 Till 33

    if(i >= 10):
        break # Because Of This I Will Print 0 Till 10


""" Continue In Python """

# Continue Is Used To Skip The Current Iteration Of The Loop

for i in range(33):
    if i % 2 == 0:
        continue  # Skip the rest of the loop's body for even numbers

    print(i)  # Will Print Only Odd Numbers from 0 Till 32
