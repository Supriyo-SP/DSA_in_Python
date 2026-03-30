n=[1,1,1,2,3,4,5]
m=[2,3,6,7,8,8,9]
l=sorted(n+m)
print(l)
frequncy_map=dict()
for num in l:
    frequncy_map[num]=frequncy_map.get(num,0)+1

key_value=frequncy_map.keys()
print(key_value)