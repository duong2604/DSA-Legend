class Node:
    def __init__(self, data):
         self.data = data
         self.next = None
         
class linkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        current_node = self.head
        while current_node.next: 
            current_node = current_node.next
        current_node.next = new_node
    
    def traversal(self):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            if current_node:
                print(current_node, end='-->')
        print()  

ll = linkedList()

node1 = ll.append(10)         
node1 = ll.append(20)         
node1 = ll.append(30)         
node1 = ll.append(40)         
node1 = ll.append(50)    
ll.traversal()
