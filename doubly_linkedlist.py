class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, node: Node):
        self.head = node
        self.tail = None

    def forward_traversal(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next

    def reverse_traversal(self):
        node = self.tail
        while node:
            print(node.data, end=' ')
            node = node.prev


head = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)

head.next = node1
node1.next = node2
node2.next = node3

node3.prev = node2
node2.prev = node1
node1.prev = head

dll = DoublyLinkedList(head)
dll.tail = node3
dll.forward_traversal()
print()
dll.reverse_traversal() 

