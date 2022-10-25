class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None
    def making_list(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
    
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    def add_end(self,data):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            new_node = Node(data)
            n.ref = new_node
    
                
                
    def printList(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
l1 = LinkedList()
n1 = int(input("Enter  a number:"))
l1.making_list(n1)
n2 = int(input("Enter  a number:"))
l1.add_begin(n2)
n3 = int(input("Enter  a number:"))
l1.add_begin(n3)
n4 = int(input("Enter  a number:"))
l1.add_begin(n4)
n5 = int(input("Enter  a number:"))
l1.add_end(n5)
n6 = int(input("Enter  a number:"))
l1.add_end(n6)
l1.printList()

