k = 0
new = []
ask=int(input("how many element"))
while (k < ask):
    user = input("enter string :")
    new.append(user)
  
    k = k+1
print("original list : " ,new)

# For Sorting
i = 0
while i < len(new):
    j = i+1
    while j < len(new):
        if new[i] > new[j]:
            var = new[i]
            new[i] = new[j]
            new[j] = var
        j = j+1

    i = i+1
print("Albhabetically list : " ,new)

a=''.join(new)
print(a)









