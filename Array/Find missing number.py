arr=[1,0,2,3,5,6,7,8,9]
n=len(arr)
frequency=dict()
for i in range(0,n+1):
    frequency[i]=0
for num in arr:
    frequency[num]=1 

for k,u in frequency.items():
    if u==0:
        ans=k
print(ans)               

    
    