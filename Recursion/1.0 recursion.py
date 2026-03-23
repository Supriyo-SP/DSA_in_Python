#infinite recursion👇
# def greet():
#     print("Hi,I am computer")
#     greet()
# greet()    

#head Recursion👇
# def func(count=0):
#     if count==5:
#         return  
#     print("hello")
#     func(count+1)   
# func()


def func(count=0):
    if count==5:
        return  
    func(count+1)   
    print("hello")    
func()

