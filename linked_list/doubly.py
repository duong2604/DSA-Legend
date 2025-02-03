class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # First node of the list

    # Insert a node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the end
            current = current.next
        current.next = new_node
        new_node.prev = current  # Link the new node to the previous node

    # Traverse forward
    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # Traverse backward
    def traverse_backward(self):
        current = self.head
        if not current:
            return
        while current.next:  # Go to the last node
            current = current.next
        while current:  # Traverse backwards
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")
    # Insert a node at the beginning
    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    # Insert a node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        
    # Insert a node at a specific position
    def insert_at_position(self, position, data):
        if position == 0:  # Insert at the beginning if position is 0
            self.insert_at_begin(data)
            return
        new_node = Node(data)
        current = self.head
        count = 0 
        
        # Traverse to the position where the node should be inserted
        while current and count < position - 1:
            current = current.next
            count += 1

        if not current:  # If position is out of bounds
            print("Position out of bounds")
            return

        # Adjust pointers to insert the new node
        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current


dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

print("Before Insertion at Position:")
dll.traverse_forward()

print("Insert at the position:")
dll.insert_at_position(2, 25)

print("After Insertion at Position:")
dll.traverse_forward()
