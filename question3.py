#Write a Python function that accepts a list and returns a new list with only the even numbers from the original list. 

l=[]

for i in range(5):
    x=int(input("Enter the integers:"))
    l.append(x)

    
evenlist=[]

for i in l:
    if(i%2==0):
        evenlist.append(i)

print("even list:",evenlist)
