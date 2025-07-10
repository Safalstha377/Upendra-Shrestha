#18.Write a program that reads a number and prints whether it is a palindrome or not. 

for n in range (0,99999999999):
 x=input("Enter a number to check palidrome or not:=")
 l=list(x)
 palindrome=False
 for i in range(len(l)//2):
    if l[i]==l[-(i+1)]:
        palindrome=True

 if palindrome:
    print(f"{x} is a palindrome number.")    

 else:
    print(f"{x} is not  a palindrome number.")  

 choice = input("\nEnter 'c' to continue or 'n' to exit:")
 if choice.lower() == 'n':
    print("Exiting the program.")
    break

