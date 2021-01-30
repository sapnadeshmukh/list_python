elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count_odd=0
sum_odd=0
count_even=0
sum_even=0
while (i<len(elements)):
    if(elements[i]%2==0):
        sum_even=sum_even+elements[i]
    else:
        sum_odd=sum_odd+elements[i]
    i=i+1
print(sum_even)
print(sum_odd)
