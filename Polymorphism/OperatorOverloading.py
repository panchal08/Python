class oo:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return self.data + other.data


obj1 = oo(100)
obj2 = oo(200)

print(obj1.__dict__)
print(obj1+obj2)
