nums=[1,99,101,98,2,5,3,100,4,6]
l=len(nums)
max_count=0
for i in range(0,l):
    num=nums[i]
    count=1
    while num+1 in nums:
        count+=1
        num+=1
    max_count=max(max_count,count)    

print(max_count)
