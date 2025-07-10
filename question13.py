#13.Write a program that reads a number and prints the factorial of that number using a while loop. 
for n in range (0,99999999999):
 x=int(input("Enter the number to get its factorial:"))
 if x<0:
    print("Factorial of",x,"does not exist.")
 elif x==0:
    print(f"Factorial of {x} is 1.")
 else:
    factorial=1
    for i in range(1,x+1):
        factorial=factorial*i
    
    print("The factorial of",x,"is",factorial)  

      
       

