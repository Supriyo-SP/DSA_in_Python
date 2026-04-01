# works for every number
arr=[0,0,1,1,1,1,1,0,1,0]
new_arr=[]
count=1
for i in range(0,len(arr)-1):
    if arr[i]!=arr[i+1]:
        count=1
    else:
        count=count+1
        new_arr.append(count)    
n=max(new_arr)
print(n)        

#another solution (optimal) for only consecutive 1's
arr=[0,0,1,1,1,1,1,0,1,0]
c=0
mc=0

for num in arr:
    if num==1:
        c+=1
    else:
        mc=max(mc,c)
        c=0
    ans=max(mc,c) 

print(ans)
            