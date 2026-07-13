class stack:
    def __init__(self):
        self.s = []

    def pop (self):
        if len(self.s ) == 0:
            raise Exception ("stack is Empty")
        else:
            return(self.s.pop())

    def push (self, data):
         self.s.append(data)
         return 
    
    def peek(self):
        if len(self.s) == 0:
             print("stack is Empty")
             return
        else:
            return(self.s[len(self.s)-1])

obj =stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
print(f"last element is {obj.peek()}")
print(f"delet {obj.pop()}")
print(f"last element is {obj.peek()}")
print(f"delet {obj.pop()}")

