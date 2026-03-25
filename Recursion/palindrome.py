def palindrome(x):
    num=x
    n=0
    while num>0:
        l=num%10
        n=(n*10)+l
        num=num/10
    return x==n  

print(palindrome(121)) 
