list=[44,4,4,5,78,67,78,56,55,5,5,5]
frequency_map=dict()
for num in list:
    frequency_map[num]=frequency_map.get(num,0)

j=0
for k in frequency_map:
    list[j]=k
    j+=1    

print(list,j)