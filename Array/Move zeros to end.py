list=[1,2,4,0,0,5,6]
for i in range(0,len(list)):
    if list[i]==0:
        for j in range(i+1,len(list)):
            if list[j]!=0:
               list[i],list[j]=list[j],list[i]
               j+=1
        i+=1              
print(list)          