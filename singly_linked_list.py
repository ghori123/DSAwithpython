class node:
    def __init__(self,data, next=None):
        self.data=data
        self.next=next

class singly_linked_list:
    def __init__(self, head=None):
        self.head=head

    def insert_at_beginning(self,data):
        temp= node(data)
        if self.head is None:
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp

    def insert_at_end(self,data):
        temp = node(data)
        if self.head is None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next != None:
                t1 = t1.next
            t1.next = temp

    def insert_at_position(self,data,x):
         temp = node(data)
         t1 = self.head 
         while t1 != None:
             if t1.data == x:
                    temp.next = t1.next
                    t1.next = temp
                    break
             t1 = t1.next

    def deleteLL(self,value):
          if self.head is None:
           print("Linked list is empty")
           return

          if self.head.data == value:
               self.head = self.head.next
               return
          t1 = self.head
          prev = t1
      
          while t1.next != None:
            if t1.data == value:
                prev.next = t1.next
                break
            prev = t1
            t1 = t1.next
          if t1.data == value:
            prev.next = None
                 
                 
    def printll(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            t1 = self.head
            while t1 != None:
                print(t1.data, end=" -->")
                t1 = t1.next
            print("None")

l1 = singly_linked_list()
l1.insert_at_end(10)
l1.insert_at_end(20)
l1.insert_at_end(30)
l1.insert_at_beginning(5)
l1.insert_at_position(15,10)        
l1.deleteLL(20)
l1.printll()