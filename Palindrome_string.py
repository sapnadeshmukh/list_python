x=input("enter any string :=")
w=[]
i=len(x)-1
while(i>=0):
    print(x[i],end="")
    w.append(x[i])
    
    i=i-1
# print(w)
a=("".join(w))
print (a)
 
if (x == a):
    print("Yes")
else:
    print("No")