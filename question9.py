# Write a Python program to remove elements from a list that are also present in another list.
m=set([10,20,30,40,50,60])
n=set([10,4,20,40])

print("new list:",m-n)

## METHOD 2:

for i in n:
    if i in m:
        m.remove(i)

print("new list by method 2:",m)
