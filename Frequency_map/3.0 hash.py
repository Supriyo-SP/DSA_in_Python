#Q : two lists are given n & m now how many times the elements of m are there in n list ?
n=[1,2,4,6,5,5,4,3,2,9,10,1,2,10,1,1] #n<=10
m=[1,10,9,34,556,23,5] 
hash_map=dict()
for num in n:
    hash_map[num]=hash_map.get(num,0)+1

for x in m:
    e= hash_map.get(x,"not found") 
    print(f"{x} : {e}") 