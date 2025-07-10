#17.Write a program to generate the Fibonacci sequence up to n terms.
n=int(input("Enter the number of terms up to which you want to get fibonacci series=="))
x=0
y=1
for num in range(n):
    print(f"{x},",end="")
    x,y=y,x+y
print("......")