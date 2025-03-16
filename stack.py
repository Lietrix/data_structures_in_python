class stack:
    def __init__(self):
        self.stack = []
        pass
    def pop(self):
        if len(self.stack) == 0:
            return
        return self.stack.pop(len(self.stack) - 1)
    def push(self, item):
        self.stack.append(item)
        
s = stack()
print("PUSH")
s.push(10)
print("1: 10")
s.push(20)
print("2: 20")
s.push(30)
print("3: 30")


print("POP")
print("1:", s.pop())
print("2:", s.pop())
print("3:", s.pop())