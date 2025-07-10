#Write a program to input key-value pairs from the user and store them in a dictionary. Allow the user to search for a key and display its value. 


prices={}
for i in range(3):
    name=input("enter the name of fruit:")
    cost=input("Enter its price:")
    prices[name]=cost

name=input("enter fruit to know its cost:")
if name in prices.keys():
    

   print(f"The cost of {name} is:{prices[name]}")
else:
    print("fruit not found:")


    
