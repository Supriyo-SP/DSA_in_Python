list =[33,89,70,52,54,33,24,26,99,98,100]
largest=float("-inf")
sLarge=float("-inf")
for num in list:
    largest=max(largest,num)

for num in list:
    t=max(sLarge,num)
    if t<largest and t!=largest:
        sLarge=t
        
print(sLarge)


