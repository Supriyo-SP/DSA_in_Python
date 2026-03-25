name=input("enter a sting: ")
def palindrome(str,left ,right):
    if left>=right:
        return True
    if str[left]==str[right]:
        return palindrome(str,left+1,right-1)
    else:
        return False

    


print(palindrome(name,0,len(name)-1))


