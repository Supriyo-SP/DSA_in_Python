class Stack:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return f"Stack({self.items})"

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "stack is empty"

        x = self.items.pop()
        return x

    def isempty(self):
        return len(self.items) == 0

    def top(self):
        if len(self.items) == 0:
            return "stack is empty"
        return self.items[-1]

stack = Stack()
stack.push(5)
stack.push(7)
stack.push(34)
print(f"{stack}")
stack.pop()
print(f"{stack}")
