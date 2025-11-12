class Stack:
    def __init__(self) -> None:
        self.stack = []
        
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if len(self.stack) == 0:
            return -1
        
        removed = self.stack.pop()
        return removed
    
    def search(self, element):
        if self.stack[element] in self.stack:
            return self.stack.index(element)
        else:
            return -1
    
    def peek(self):
        return self.stack[-1]
    
    def empty(self):
        if not self.stack:
            return -1
    
    def full(self, max_size):
        return len(self.stack) == max_size