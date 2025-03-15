class queue:
    def __init__(self):
        self.queue = []
        pass
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) == 0:
            return
        return self.queue.pop(0)
    
q = queue()
print("ENQUEUE")
q.enqueue(10)
print("1: 10")
q.enqueue(20)
print("2: 20")
q.enqueue(30)
print("3: 30")


print("DEQUEUE")
print("1:", q.dequeue())
print("2:", q.dequeue())
print("3:", q.dequeue())