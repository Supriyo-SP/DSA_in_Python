list1=[44,4,4,5,78,67,78,56,55,5,5,5]
frequency_map=dict()
for num in list1:
    frequency_map[num]=frequency_map.get(num,0)

keys_view = frequency_map.keys()
print( keys_view )

