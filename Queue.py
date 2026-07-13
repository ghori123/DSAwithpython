class Queue:
    def __init__(self):
        self.items =[]

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
        
    def insert(self,data):
        self.items.append(data)
        return
    
    def delete(self):
        if len(self.items) == 0:
            raise Exception("Queue is Empty")
        else:
          return  self.items.pop(0)
        
Q = Queue()
print(f"is queue is empty: {Q.isEmpty()}")
Q.insert(10)
Q.insert(20)
Q.insert(30)
Q.insert(40)
print(f"is queue is empty: {Q.isEmpty()}")

print(f"delet first element: {Q.delete()}")
print(f"delet first element: {Q.delete()}")