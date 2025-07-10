

#5.Create a set of prime numbers less than 50. Write a program to check whether a given number exists in the set or not. 

prime=[]
for num in range(1,51):
    count=0
    for i in range(1,num+1):
        if(num%i==0):
            count+=1
    if(count==2):
        prime.append(num)


print(prime)        

x=int(input('enter a number'))
if x in prime:
   
    print("Number found.")

if x not in prime:
    print("Number not found.")    
