list=[1,5,6,4,5,1,6,8,9,9,1,5,1]
frequency_map=dict()
for i in range(0,len(list)):
    frequency_map[list[i]]=frequency_map.get(list[i],0)+1

print(frequency_map[5])    