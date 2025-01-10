from function import *

# Example Usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(4)
ll.append(5)
ll.append(6)

print("Original List:")
ll.traverseAndPrint()  # Outputs: 1 -> 2 -> 3 -> null

# ll.reverse()  # Reverse the linked list

# print("Reversed List:")
# ll.traverseAndPrint()  # Outputs: 3 -> 2 -> 1 -> null

# Find index of a node
# index = ll.findIndexOfNode(2)
# print(">>>>>>>>>>>>>>>>>> index of node:" , index)  

# ll.deleteNode(3)

ll.insert_at_begin(3)

ll.traverseAndPrint()