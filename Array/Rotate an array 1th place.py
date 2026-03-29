#using Slicing
# list=[2,6,7,8,4,9]
# n=len(list)
# list[:]= [list[-1]] + list[0:n-1]
# print(list)

#using Loop
list=[2,6,7,8,4,9]
n=len(list)
temp=list[n-1]
for i in range(n-2,-1,-1):
    list[i+1]=list[i]
list[0]=temp
print(list)

