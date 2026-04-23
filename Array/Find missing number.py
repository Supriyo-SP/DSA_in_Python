# arr=[1,0,2,3,5,6,7,8,9]
arr=[4,3,2,7,8,2,3,1]
arr.sort()
n=len(arr)
frequency=dict()
ans=[]
for i in range(arr[0],n+1):
    frequency[i]=0
for num in arr:
    frequency[num]=1 

for k,u in frequency.items():
    if u==0:
        ans.append(k)
print(ans)               

    
    