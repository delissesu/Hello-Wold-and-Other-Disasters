from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional['Node'] = None
    
class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        
    def pop(self):
        if not self.top:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.pop())
print(s.pop())