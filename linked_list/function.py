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
        if self.is_empty():
            print("The list is empty.")
            return

        if self.head.data == data:
            self.head = self.head.next
            return
        
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next
        
        if current_node.next is None:
            print("Node not found.")
            return
        else:
            current_node.next = current_node.next.next
        

# Example Usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)

print("Original List:")
ll.traverseAndPrint()  # Outputs: 1 -> 2 -> 3 -> null

ll.reverse()  # Reverse the linked list

print("Reversed List:")
ll.traverseAndPrint()  # Outputs: 3 -> 2 -> 1 -> null

# Find index of a node
index = ll.findIndexOfNode(2)
print(">>>>>>>>>>>>>>>>>> index of node:" , index)  

ll.deleteNode(3)
ll.traverseAndPrint()