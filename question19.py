#19.Write a program that finds all numbers between 100 and 999 where the sum of the cubes of the digits equals the number itself (Armstrong numbers).

armstrong_numbers=[]
for num in range(100,1000):
    digits=list(str(num))
    sum=0
    for i in range(len(digits)):
     sum+=int(digits[i])**3
    if sum==num:
        armstrong_numbers.append(num)

print(armstrong_numbers)        





        

    

    
    