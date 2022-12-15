import pickle
class Employee:

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print(self.id, '\t', self.name, '\t', self.salary)


with open('Test_new.txt', 'wb') as w:
    e = Employee(11001, 'Mark', 34256)
    f = Employee(11002, 'John', 45376)
    pickle.dump(e, w)
    pickle.dump(f, w)
    print('Pickle done')

with open('Test_new.txt', 'rb') as r:
    obj = pickle.load(r)
    print('Unpickle done')
    obj.display()
