n=[1,1,1,2,3,4,5]
m=[2,3,6,7,8,8,9]
l=sorted(n+m)
print(l)
frequncy_map=dict()
for num in l:
    frequncy_map[num]=frequncy_map.get(num,0)+1

key_value=frequncy_map.keys()
print(key_value)

#Another Method (optimal)
    
n = [1,1,1,2,3,4,5]
m = [2,3,6,7,8,8,9]

i = 0
j = 0
result = []
l1 = len(n)
l2 = len(m)

while i < l1 and j < l2:
    if n[i] < m[j]:
        val = n[i]
        i += 1
    elif m[j] < n[i]:
        val = m[j]
        j += 1
    else:
        val = n[i]
        i += 1
        j += 1

    if len(result) == 0 or result[-1] != val:
        result.append(val)

while i < l1:
    if len(result) == 0 or result[-1] != n[i]:
        result.append(n[i])
    i += 1

while j < l2:
    if len(result) == 0 or result[-1] != m[j]:
        result.append(m[j])
    j += 1

print(result)
