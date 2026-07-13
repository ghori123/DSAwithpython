class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.item =[None]*size
        self.front = self.rear = -1

    def enqueue(self,data):
        if ((self.rear+1) % self.size) == self.front:
            print("Queue is Full")
        elif (self.front== -1):
            self.front= self.rear =0
            self.item[self.front] = data
            return
        else:
            self.rear = (self.rear+1)% self.size
            self.item[self.rear]= data
            return

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
        elif self.front == self.rear:
            print(self.item[self.front])
            self.front=self.rear = -1
            return
        else:
            print (self.item[self.front])
            self.front = (self.front +1)% self.size
            return

Q = CircularQueue(5)
Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
Q.enqueue(40)
Q.enqueue(50)
print(f"deleted element is {Q.dequeue()} ")
Q.enqueue(60)
Q.enqueue(70)
