
def duplicate_element(array_nums):
    nums_set = set(array_nums)    
    return len(array_nums) != len(nums_set)     
user=[1,2,8,3,4,5,6,1]

print(duplicate_element(user))

print("****************")

def dup(user1):
    i=0
    new=[]  
    while i<len(user1):
        if user1[i] not in new:
            new.append(user1[i])
        i=i+1
    print(new)
user=[1,3,6,9,8,66,6,3,8]
dup(user)