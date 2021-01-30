elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count_odd=0
sum_odd=0
average_even=0
count_even=0
sum_even=0
average_odd=0
while (i<len(elements)):
    if(elements[i]%2==0):
        count_even=count_even+1

        sum_even=sum_even+elements[i]
    else:
        sum_odd=sum_odd+elements[i]
        count_odd=count_odd+1

    i=i+1
print (count_even)
print(count_odd)
print(sum_even)
print(sum_odd)
average_even=sum_even//count_even
average_odd=sum_odd//count_odd
print (average_even)
print(average_odd)
