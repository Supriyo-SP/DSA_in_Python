# list=[1,5,6,4,5,1,6,8,9,9,1,5,1]
list = ["✅", "✅", "✅", "😥", "😭", "😭", "👍", "👍", "👍", "😂"]
frequncy_map=dict()
for i in range (0,len(list)):
    if list[i] in frequncy_map:
        frequncy_map[list[i]]+=1
    else:
        frequncy_map[list[i]]=1    

print(frequncy_map["✅"])
#succesfully executed ✅
#O(n) - time & space complexity