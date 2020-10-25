class cons:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def sum(self,d):
         return self.a+self.b+d
    def sub(self):
        return self.a-self.b

c=cons(3,2)

print(c.sum(5))
print(c.sub())