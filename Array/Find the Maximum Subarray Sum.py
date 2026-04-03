#Brute Force solution
arr=[-2,-1,-3,4,-1,2,1,-5,4]
maxi=float("-inf")
for i in range(0,len(arr)):
    total=0
    for j in range(i,len(arr)):
        total=total+arr[j]
        maxi=max(maxi,total)
    ans=maxi 
print(maxi) 
#optimal solution
arr=[-2,-1,-3,4,-1,2,1,-5,4]
maxi=float("-inf")
total=0
for i in range(0,len(arr)):
    total=total+arr[i]
    maxi=max(maxi,total)
    if total<0:
        total=0
    ans=maxi
           
