class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linked_list(head):
    new = head
    while new is not None:
        print(new.data, end=" -> ")
        new = new.next
    print("None")

start = Node(62)
node2 = Node(72)
node3 = Node(34)
node4 = Node(90)
node5 = Node(51)

start.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print_linked_list(start)
