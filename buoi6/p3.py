class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def isEmpty(self):
        return len(self.data) == 0

    def isFull(self):
        return len(self.data) == self.capacity

    def pop(self):
            if self.isEmpty():
                print("Stack rỗng")
            return self.data.pop()

    def push(self, value):
        if self.isFull():
            print("Stack đầy")
        return self.data.append(value)
        
    def top(self):
        if self.isEmpty():
            return None
        return self.data[-1]


stack1 = MyStack(capacity=5)
stack1.push(2)
stack1.push(4)

print(stack1.isFull())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.isEmpty())
