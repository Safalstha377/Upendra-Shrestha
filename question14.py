#14.Write a program to print the multiplication table of a given number using a for loop. 
x=int(input("Enter the number to find its multipication table:"))
res=x
for i in range(1,11):
    res=x*i
    
    print(f"|{x}*{i}={res}|")
    

    