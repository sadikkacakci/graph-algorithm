# python dosyalarıyla overriding olmaması için myQueue olarak dosya ismini kaydettim.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty.")
            return
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            print("Queue is empty" )
            return        
        return self.items[0]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
