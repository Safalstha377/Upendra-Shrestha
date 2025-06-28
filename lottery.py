import random

user = []
print("Pick 3 numbers (1 to 49):")

while len(user) < 3:
    n = input("Enter a number: ")
    if n.isdigit():
        n = int(n)
        if 1 <= n <= 49 and n not in user:
            user.append(n)
        else:
            print("Number must be 1-49 and not repeated.")
    else:
        print("Please enter a number.")

lottery= []
while len(lottery) < 3:
    r = random.randint(1, 49)
    if r not in lottery:
        lottery.append(r)

print("Your numbers:", user)
print("Lottery numbers:", lottery)

match = 0
i = 0
while i < 3:
    if user[i] in lottery:
        match = match + 1
    i = i + 1

print("You matched", match, "number(s).")

if match == 3:
    print(" You won!")
else:
    print("Better luck next time.")
    





    
