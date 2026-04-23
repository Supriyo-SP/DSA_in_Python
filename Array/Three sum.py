nums = [-1,0,1,2,-1,-4]
s=set()
for i in range(0,len(nums)):
    for j in range (i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[k]==0:
                temp=[nums[i],nums[j],nums[k]]
                temp.sort()
                s.add(tuple(temp))
print(s)