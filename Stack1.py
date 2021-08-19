class Stack:
    def __init__(self):
        self.data=[]

#Checking length of stack
    def len(self):
        return len(self.data)

#Check stack is empty
    def is_empty(self):
        return len(self.data)==0

#Insert element into stack
    def push(self, element):
        self.data.append(element)

#Checking stack is empty or not and delete element
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.data.pop()

#Display element from stack
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.data[-1]


s= Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)

print(s.data)

print(s.is_empty())

print(s.pop())
print(s.data)
print(s.pop())
print(s.data)

print(s.display())  #Display top most element of stack