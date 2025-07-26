# Definition of a Node in LinkedList
class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        temp = self.head
        while temp is not None:
            yield temp
            temp = temp.next

    def insert_at_start(self, data: int):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        else:
            self.head = new_node

    def remove_head(self):
        if self.head:
            self.head = self.head.next

    def traverse_recursive(self, node):
        if node:
            print(node.data, end=' ')
            self.traverse_recursive(node.next)
        return

head = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)

head.next = node1
node1.next = node2
node2.next = node3

ll = LinkedList()
ll.head = head

for node in ll:
    print(node, end=' ')
print()

print("Add new node 5 at the start.")
ll.insert_at_start(5)

for node in ll:
    print(node, end=' ')
print()

print("Add new node 6 at the start.")
ll.insert_at_end(6)
for node in ll:
    print(node, end=' ')
print()

print("Recursive traversal: ")
ll.traverse_recursive(ll.head)