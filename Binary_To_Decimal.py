binary=[1,0,0,1,1,0,1,1]
a=len(binary)-1
count=0
caculator=1
while (a>=0):
    count=count+(binary[a])*caculator
    caculator=caculator*2
    a=a-1
print(count)