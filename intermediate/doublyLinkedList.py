class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("None")

def print_linked_list_reverse(tail):
    temp = tail
    while temp is not None:
        print(temp.data, end=" <-> ")
        temp = temp.prev
    print("None")

node1 = Node(62)
node2 = Node(72)
node3 = Node(34)
node4 = Node(90)
node5 = Node(51)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev = node4

print_linked_list(node1)
print_linked_list_reverse(node5)
