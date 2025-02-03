class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def traversal(self):
        if self.head is None: 
            return
        curr = self.head
        while curr:
            print(curr.data, end="")
            curr = curr.next
            if curr:
                print(" --> ", end="")
        print()  # For a newline after traversal

# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.append(60)
ll.traversal()
