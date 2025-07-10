#15.Write a program to find the largest and smallest number in a list entered by the user. 
m= input("Enter integers separated by spaces: ")
x = [int(num) for num in m.split()]
greatest=x[0]
for num in x[1:]:
  if num>greatest:
   greatest=num
print(f"The greatest number in the list is: {greatest}")

smallest=x[0]
for num in x[1:]:
  if num<smallest:
    smallest=num
print("The smallest number in the list is:",smallest)


