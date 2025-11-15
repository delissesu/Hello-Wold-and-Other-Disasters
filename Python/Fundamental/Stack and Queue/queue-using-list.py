class Queue:
    def __init__(self) -> None:
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enq(self, item):
        self.items.insert(0, item)
    
    def deq(self):
        return self.items.pop()

