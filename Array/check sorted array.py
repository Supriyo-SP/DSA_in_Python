list=[1,3,5,7,11,1,13,15]
for i in range (0,len(list)-1):
    if list[i]<list[i+1]:
        boolan=True
    else:
        boolan=False
        break  

print(boolan)       