# Definition of a Node in LinkedList
class Node:
    def __init__(self, data: object):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next



head = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)

head.next = node1
node1.next = node2
node2.next = node3

ll = LinkedList()
ll.head = head

ll.traverse_list()

