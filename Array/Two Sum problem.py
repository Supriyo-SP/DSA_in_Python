#Brute Force Solution
# arr=[5,9,1,2,4,15,6,3]
# target=13
# ans=[]
# for i in range(0,len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]+arr[j]==target:
#             ans.append(i)
#             ans.append(j)
#             break

# print(ans)

#Better Optimal Solution:
arr=[5,9,1,2,4,15,6,3]
hash_map=dict()
target=13
ans=[]
for i in range(0,len(arr)):
    remaining=target-arr[i]
    if remaining in hash_map:
        ans=[hash_map[remaining],i]
    hash_map[arr[i]]=i

print(ans)    


