list=[1,2,3,4,5,6]
n=len(list)
i=int(input("enter k "))
for j in range(0,i):
    list[:]=[list[-1]]+list[0:n-1]
print(list)    