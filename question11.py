#11.Write a program to check whether a given number is prime or not.


 
for n in range(0,9999999999999):
   
 x=int(input("Enter the integer to check prime or not:" ))
 if x<=1:
    print(x,"is not prime number")
    
 else:
   prime=True
   for i in range(2,x):
    if(x%i==0):
     prime=False
     break
     
   if prime==True:
    print(x,"is a prime number")
   else:
    print(x,"is not a prime number")
        

        


