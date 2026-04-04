nums = [3,1,-2,-5,2,-4]
l=len(nums)
result=[0]*l
p=0
n=1
for i in range(0,l):
    if nums[i]>=0:
        result[p]=nums[i]
        p+=2
    else:
        result[n]=nums[i]
        n+=2

print(result)            