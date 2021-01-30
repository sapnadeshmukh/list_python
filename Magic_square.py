magic_square = [[8, 3, 4],
                [1, 5, 9],
                [6, 7, 2]]


#sum of row elements#
i=0
while(i< len(magic_square)):
    j=0
    sum1=0
    while (j<len(magic_square[i])):
        sum1=sum1+magic_square[i][j]
        
        j=j+1
    i=i+1

print("sum of row elements:=" ,sum1)

#sum of column elements#
i=0

while i<len(magic_square):
	j=0
	sum2=0
	while j<len(magic_square[i]):
		sum2=sum2+magic_square[j][i]
		j=j+1
	
	i=i+1
print ("sum of column elements := ",sum2)

# sum of left to right diagonals#
i=0
j=0
sum3=0
while (i<len(magic_square)):
    new=(magic_square[i][j])
    sum3=sum3+new
    i=i+1
    j=j+1
    
print("sum of diagonals from left to right :=",sum3)          


# sum of right to left diagonals
magic_square=[[8,3,4],[1,5,9],[6,7,2]]
i=0
new=0
j=2
sum4=0
while i<len(magic_square):
    new=(magic_square[i][j])
    sum4=sum4+new
    j=j-1
    i=i+1
print ("sum of diagonal from right to left:=", sum4)



if (sum1==sum2)and (sum3==sum4):
    print("Magic Square")
else:
    print("Not magic square")