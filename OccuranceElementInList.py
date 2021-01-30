# by function
def countX(lst, x): 
    count = 0
    for i in list_num: 
        if (i == x): 
            count = count + 1
    return count 
  
list_num = [8, 6, 8, 10, 8, 20, 10, 8, 8,2,1,2,1,1,1] 
x = 1
print(countX(list_num, x))

# by loop

list_num = [8, 6, 8, 10, 8, 20, 10, 1,2,1,2,1,1,1] 
x = 8
count=0
i=0
for i in list_num:
    if (i==x):
        count=count+1
    i=i+1
print(count)
