#print the upper diagonal
nums=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,len(nums)):
    for j in range(0,len(nums[0])):
        if  j>=i:
            
            print(nums[i][j],end=" ")
        else:
            print("*",end=' ')    
    print()

#print diagonal
for i in range(0,len(nums)):
    for j in range(0,len(nums[0])):
        if  j==i:
            
            print(nums[i][j],end=" ")
        else:
            print("*",end=' ')    
    print()     
