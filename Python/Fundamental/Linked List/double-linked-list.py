from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None

# A ↔ B ↔ C
A = Node('A')
B = Node('B')
C = Node('C')
A.next = B
B.prev = A
B.next = C
C.prev = B

# hapus B
A.next = C
C.prev = A
del B
