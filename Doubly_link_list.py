class node :
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class doubly_linked_list :
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        temp = node(data)
        if self.head is None:
            self.head = temp
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

    def insert_at_end(self, data):
        temp = node(data)
        if self.head is None:
            self.head = temp
        else:
            self.t1 = self.head
            while self.t1.next != None:
                self.t1 = self.t1.next
            self.t1.next = temp
            temp.prev = self.t1

    def insert_at_position(self, data, x):
        temp = node(data)
        if self.head is None:
            self.head = temp
        else:
            self.t1 = self.head
            while self.t1.next != None:
              if self.t1.data == x:
                temp.next = self.t1.next
                temp.prev = self.t1
                self.t1.next.prev = temp
                self.t1.next = temp
                return
              self.t1 = self.t1.next

    def deleteDll(self, value):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == value:
            self.head =self.head.next
            self.head.prev = None
            return
        
        self.t1 = self.head
        while self.t1.next != None:
            if self.t1.data == value:
                 self.t1.prev.next = self.t1.next
                 self.t1.next.prev = self.t1.prev
                 return
            self.t1 = self.t1.next
        if self.t1.data == value:
            self.t1.prev.next = None
            self.t1.prev = None
            return


    def printDll(self):
        if self.head is None:
            print("List is empty")
        else:
            self.t1 = self.head
            while self.t1 != None:
                print(self.t1.data, end=" <---> ")
                self.t1 = self.t1.next
            print("None")

D1 = doubly_linked_list()
D1.insert_at_end(10)
D1.insert_at_end(20)
D1.insert_at_end(30)
D1.insert_at_end(35)
D1.insert_at_end(40)
D1.insert_at_beginning(5)
D1.insert_at_position(25, 20) 
D1.deleteDll(5)
D1.deleteDll(40)
D1.deleteDll(25)
D1.printDll()