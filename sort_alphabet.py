a=["xmas","zerox","dog","banana","apple","cat","yellow"]
b=len(a)
new=[]
i=0
while (i<b):
    c=min(a)
    new.append(c)
    a.remove(c)
    i=i+1
print(new)