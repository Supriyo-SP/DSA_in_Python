#Tail Recursion 👇
def func(x,n):
    if x>n:
        return 
    func(x+1,n) 
    print(n-x+1)
    
func(1,15) 
#head Recursion👇
def head(x,n):
    if x>n:
        return
    print(x)
    head(x+1,n)
head(1,8)       