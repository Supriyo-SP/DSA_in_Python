arr=[1,2,3,5,6,-10,1,4,78]
j=int(input("enter the elemnt which you want to search :"))
def find_index(n,arr):
    for i in range(0,len(arr)):
        if arr[i]==n:
            return i
    return -1    
        
        
print(find_index(j,arr))        



