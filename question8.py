# Given a list of names, write a program to count how many times each name appears using a dictionary. 


names=["a","b","c","d","a","b","c"]
d={}

for name in names:
    if name not in d.keys():
        d[name]=names.count(name)

print(d)        
