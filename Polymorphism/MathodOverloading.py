class MethodOverloading:
    def addition(*args):
        add = 0
        for item in args[1:]:
            add = add + item
        return add


if __name__ == '__main__':
    result = MethodOverloading().addition(2, 3, 4, 8, 5)
    print(result)
