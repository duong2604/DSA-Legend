class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        """Check if the linked list is empty."""
        return self.head is None

    def append(self, data):
        """Add a new node with the given data to the end of the linked list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
    
    def traverseAndPrint(self):
        """Traverse the linked list and print its elements."""
        if self.is_empty():
            print("The list is empty.")
            return
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("null")
        
        
    def findIndexOfNode(self, data):
        if self.is_empty():
            print("The list is empty.")
            return
        current_node = self.head
        index = 0
        while current_node:
            if current_node.data == data:
                return index
            current_node = current_node.next
            index += 1
       

    def reverse(self):
        """Reverse the linked list in place."""
        if self.is_empty():
            print("The list is empty; nothing to reverse.")
            return
        prev = None
        current_node = self.head
        while current_node:
            next_node = current_node.next  # Save the next node
            current_node.next = prev  # Reverse the link
            prev = current_node  # Move prev to the current node
            current_node = next_node  # Move to the next node
        self.head = prev  # Update head to the new front of the list

    def deleteNode(self, data):
        if self.head is None:
            return
      
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next
    
        if current_node is None:
            return self.head
        
        current_node.next = current_node.next.next

    # Insert a node at the beginning of the linked list
    def insert_at_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    
    
    # Insert a node at the end of the linked list
    def insert_at_the_end(self,data):
        new_node = Node(data)
        
        if self.head is None:  
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        
    def insert_node(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        for _ in range(position - 1):
            if current_node is None:
                return
            current_node = current_node.next
        
        new_node.next = current_node.next
        current_node.next = new_node
        
        
     
    
    

# Example Usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(4)
ll.append(5)
ll.append(6)

print("Original List:")
ll.traverseAndPrint()  

# ll.insert_at_begin(3)
# ll.insert_at_the_end(20)

ll.insert_node(32, 2)


ll.traverseAndPrint()