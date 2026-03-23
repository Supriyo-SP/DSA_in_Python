# same question as 3.0 hash.py but now for strings 
s="aasdddfaaeghinnm"
m=["a","s","e","n","r"]
hash_map=dict()
for char in s:
    hash_map[char]=hash_map.get(char,0)+1

for x in m:
    e= hash_map.get(x,"not found") 
    print(f"{x} : {e}")     