from __future__ import annotations
from typing import Optional

class Node:
    def __init__(self, data: int, next: Optional['Node'] = None):
        self.data = data
        self.next = next

# buat node
head = Node(10)
second = Node(20)
third = Node(30)

# sambungkan node
head.next = second
second.next = third

# traversal
current = head
while current is not None:
    print(current.data)
    current = current.next
    
# Another Example
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# # buat list: A → B → C
# head = Node('A')
# head.next = Node('B')
# head.next.next = Node('C')

# # hapus node 'B'
# prev = head
# current = head.next
# if current.data == 'B':
#     prev.next = current.next  # lewati 'B'
#     del current               # hapus node