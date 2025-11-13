from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next : Optional['Node'] = None

# A → B → C → (kembali ke A)
A = Node('A')
B = Node('B')
C = Node('C')
A.next = B
B.next = C
C.next = A

# hapus B
A.next = C
del B
