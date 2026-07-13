class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Circular_linked_list:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        temp=node(data)
        if self.head is None:
            self.head=temp
            temp.next=self.head
        else:
            t1=self.head
            while t1.next!=self.head:
                t1=t1.next
            temp.next=self.head
            self.head=temp
            t1.next=self.head

    def insert_at_end(self,data):
        temp=node(data)
        if self.head is None:
            self.head=temp
            temp.next=self.head
        else:
            t1=self.head
            while t1.next!=self.head:
                t1=t1.next
            t1.next=temp
            temp.next=self.head

    def insert_at_position(self,data,x):
        temp=node(data)
        if self.head is None:
            self.head=temp
            temp.next=self.head
        else:
            t1=self.head
            while t1.next!=self.head:
                if t1.data==x:
                    temp.next=t1.next
                    t1.next=temp
                    return
                t1=t1.next

    def deleteCLL(self,value):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data==value:
            t1=self.head
            while t1.next!=self.head:
                t1=t1.next
            t1.next=self.head.next
            self.head=self.head.next
            return
        t1=self.head
        prev=t1
        while t1.next!=self.head:
            if t1.data==value:
                prev.next=t1.next
                return
            prev=t1
            t1=t1.next
        if t1.data == value:
             prev.next = self.head
             return

    def printll(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            t1 = self.head
            while True:
                print(t1.data, end=" -->")
                t1 = t1.next
                if t1 is self.head:
                  break
            print(t1.data)

obj = Circular_linked_list()
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.insert_at_end(40)
obj.printll()
obj.insert_at_position(35, 30)
obj.insert_at_beginning(50)
obj.printll()
obj.deleteCLL(50)
obj.deleteCLL(40)
obj.deleteCLL(20)
obj.printll()