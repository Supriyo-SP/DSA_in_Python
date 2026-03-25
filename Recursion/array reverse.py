# Q: A array is given , we have to amke a func that receive the start and end index and reverese that part od=f the given array 
def reverse(arr,left,right):
    if left>=right:
        return
    arr[left],arr[right]=arr[right],arr[left]
    return reverse(arr,left+1,right-1)

arr=[1,2,3,4,5,6,7,8]
reverse(arr,0,7)
print(arr)

     
   