class Deque:
    def __init__(self):
        self.items =[]

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
        
    def insert_at_end(self,data):
        self.items.append(data)
        return
    
    def insert_at_frent(self,data):
        self.items.insert(0,data)
        return
    
    def delete_at_frent(self):
        if len(self.items) == 0:
            raise Exception("Deque is Empty")
        else:
          return  self.items.pop(0)
        
    def delete_at_end(self):
        if len(self.items) ==0:
            raise Exception("Deque is Empty")
        else:
            return self.items.pop(len(self.items)-1)
        
Q = Deque()
print(f"is Deque is empty: {Q.isEmpty()}")
Q.insert_at_end(20)
Q.insert_at_frent(10)
Q.insert_at_end(30)
Q.insert_at_end(40)
print(f"is Deque is empty: {Q.isEmpty()}")

print(f"delet first element: {Q.delete_at_frent()}")
print(f"delet first element: {Q.delete_at_frent()}")
print(f"delet last element: {Q.delete_at_end()}")
print(f"delet last element: {Q.delete_at_end()}")
print(f"is Deque is empty: {Q.isEmpty()}")