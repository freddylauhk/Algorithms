class Stack:
    # Initializer
    def __init__(self):
        self.stack = []
    
    # Empty the stack
    def Empty(self):
        self.stack = []
    
    # Return the number of element in stack
    def Size(self):
        return len(self.stack)
    
    # Return the top element in stack
    def Top(self):
        if(len(self.stack) == 0):
            print("Unable to top element from empty stack")
        else:
            return self.stack[len(self.stack) - 1]

    # Remove the top element
    def Pop(self):
        if(len(self.stack) == 0):
            print("Unable to pop element from empty stack")
        else:
            self.stack.pop(len(self.stack) - 1)

    # Push a element to stack
    def Push(self, value):
        self.stack.append(value)
    
def main():
    mystack = Stack()
    mystack.Push(3)
    mystack.Push(2)
    mystack.Push(1)
    print(mystack.stack)
    print(mystack.Size())
    print(mystack.Top())
    mystack.Pop()
    print(mystack.stack)
    print(mystack.Size())
    print(mystack.Top())
    mystack.Empty()
    print(mystack.stack)
    print(mystack.Size())
    print(mystack.Top())

if __name__ == "__main__":
    main()
