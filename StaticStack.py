#StaticStack

class StaticStack:
    def __init__(self,length):
        self.stackItems = []
        self.length = length
    def isEmpty(self):
        if len(self.stackItems)==0 :
            return True
    def isFull(self):
        if len(self.stackItems)==self.length :
            return True
    def push(self,value):
        if not self.isFull() :
            self.stackItems.append(value)
    def pop(self):
        if not self.isEmpty() :
            self.stackItems.pop()
    def peek(self):
        if not self.isEmpty():
            return self.stackItems[-1]
            
Stack1 = StaticStack(10)

if Stack1.isEmpty():
    print("Stack is Empty")
    print("")

for i in range(1,12):
    if not Stack1.isFull():
        Stack1.push(i)
        print("Item ",Stack1.peek()," is Pushed in Stack")
    else:
        print("")
        print("Stack is Full...Item ",i," cannot be inserted in Stack")

print("")
print("Peek Value in Stack : ",Stack1.peek())
print("")

for i in range(1,12):
    if not Stack1.isEmpty():
        print("Item ",Stack1.peek()," is Popped from Stack")
        Stack1.pop()
    else:
        print("")
        print("Stack is Empty...Cannot POP items from stack")
        print("")
        
if Stack1.isEmpty():
    print("Empty Stack : ",Stack1.stackItems)

print("")
Stack1.push(1)
print("Item ",Stack1.peek()," is pushed in Stack")

if not Stack1.isEmpty() and not Stack1.isFull():
    print("Stack is Neither Empty nor Full")


            
        
            
    

