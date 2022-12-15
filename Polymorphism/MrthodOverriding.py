class Parent:
    def paise(self):
        print(10000000)


class Child(Parent):
    def paise(self):
        print(20000000)


if __name__ == '__main__':
    Child().paise()
    Parent().paise()