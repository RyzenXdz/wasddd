# elif in python means [else if]. An if statements can be chained together with a lot of these elif statements followed by an else statement.

let = int(input("Enter Your Age: "))

if(let > 18):
    print("You Can Drive")

elif(let <= 17):
    print("You Are Too Old To Drive")

else:
    print("Enter The Valid Age")