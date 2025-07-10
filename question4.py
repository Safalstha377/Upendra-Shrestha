# Write a program to count the number of each character in a given string using a dictionary. 


s=input("Enter sample string:")
d={}
for i in s:
    if i not in d.keys():
      d[i]=s.count(i)

print(d)




