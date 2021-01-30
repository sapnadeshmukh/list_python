a=[50,40,23,70,56,12,5,10,7,123,200,300]
i=0
max=0
second_max=0
while (i<len(a)):
    if a[i]>max:
        max=a[i]
    i=i+1
    j=0
    while (j<len(a)):
        if (max > a[j] and second_max <a[j]):
            second_max=a[j]
        j=j+1
        

print (max)
print(second_max)