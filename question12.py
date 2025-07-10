#12.Write a program to print all the even numbers between 1 and 100 using a loop. 
x=[]
for num in range(1,100):
    if(num%2==0):
        x.append(num)
print(x)