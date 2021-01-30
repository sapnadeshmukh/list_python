elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count_odd=0
count_even=0
count_odd_even=0
sum_even=0
sum_odd=0
sum_even_odd=0
average_even=0
average_odd=0
average_even_odd=0
while (i<len(elements)):
    if (elements[i]%2==0):
        count_even=count_even+1
        sum_even=sum_even+elements[i]
        average_even=sum_even//count_even
    else:
        count_odd=count_odd+1
        sum_odd=sum_odd+elements[i]
        average_odd=sum_odd//count_odd
    i=i+1
print ("even numbers ka count " + str(count_even)   +"  hai")
print ("odd numbers ka count " + str(count_odd )+ " hai")
print ("saare numbers ka count" + str(count_even+count_odd) + " hai")
print("even numbers ka sum " + str(sum_even) + " hai")
print("odd numbers ka sum "+str(sum_odd) +"  hai")
print("saare numbers ka sum "+str(sum_even+sum_odd)+" hai")
print ("even numbers ka average " + str(average_even)+"  hai")
print("odd numbers ka average"+ str(average_odd) +" hai")
print("saare numbers ka average"+str(average_even+average_odd)+" hai")

