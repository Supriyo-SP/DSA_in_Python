from array import *
# import array as arr
val =array("i",[])
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    x=int(input("Enter element %d:" % (i+1)))      
    val.append(x)
for x in val:
    print(x,end="")    
# for i in range(0,len(val)):
#     print(val[i],end=" ")
# for x in val:
#     print(x,end=",")
# val.insert(1,50)
# print("\n")
# for x in val:
#     print(x,end=",")
# # val.reverse()
# # print("\n")
# # for x in val:
# #     print(x,end=",")
# copyArray=array(val.typecode,(a for a in val))
# print("\n")
# for x in copyArray:
#     print(x,end=",")