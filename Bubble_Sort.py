list=[1,7,4,2,9,3]
i=0
temp=0
while (i<len(list)):
    j = i+1
    while(j<len(list)):
        if(list[i]>list[j]) :
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
        j=j+1
    i=i+1
print(list)
