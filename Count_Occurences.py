char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i = 0
new_list=[]
while i < len(char_list):
    count=0
    j=0
    while j < len(char_list):
        if char_list[i]==char_list[j]:
       		count=count+1
       	j=j+1
    if [char_list[i],count] not in new_list:
    	new_list.append([char_list[i],count])
    i=i+1
print (new_list)