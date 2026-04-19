class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

node1=Node(2)
node2=Node(4)
node1.next=node2
print(node1.next)
print(node2)