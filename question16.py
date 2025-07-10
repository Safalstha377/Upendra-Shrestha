#16.Write a program that accepts 10 integers from the user and counts how many are positive, negative, and zero. 
print("Enter the 10 integers one by one")
l=[]
for num in range(1,11):
    x=(int(input(f"Enter integer no.{num}==")))
    l.append(x)

count_negative=0
count_positive=0
count_zero=0

for num in l:
    if num<0:
        count_negative+=1
    elif num>0:
        count_positive+=1
    else:
        count_zero+=1

if count_negative==1:
 print(f"Only one is negative.")        
else:
    print(f"{count_negative} are negative.")

if count_positive==1:    
   print("Only 1 is postive.")
else:
   print(f"{count_positive} are postive.") 

if count_zero==1:
   print("only one is zero")
else:   
   print(f"{count_zero} are zeros.")






