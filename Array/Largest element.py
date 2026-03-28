list =[33,89,70,52,54,33,24,26,99]
l=len(list)
large=list[0]
for i in range(0,l):
    large=max(large,list[i])
print(large)    
