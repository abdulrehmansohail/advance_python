# 7. Write a Python program to create a class representing a linked list data structure.
# Include methods for displaying linked list data, inserting and deleting nodes.

#Singly linked list is the simplest type of linked list in which every node contains some data and a pointer
# to the next node of the same data type.

class Node:
    """
        each node stores the data and the address of the next node
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
        You have to start somewhere, so we give the address of the first node a special name called HEAD
    """

    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next

        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current:
            prev.next = current.next


linked_list = LinkedList()

# Insert elements into the linked list
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)