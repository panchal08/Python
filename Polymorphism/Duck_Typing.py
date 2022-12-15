class Car:
    def engine(self):
        print('Car has 4 tor generate power')


class Bus:
    def engine(self):
        print('Bus has 6 tor generate power')


class Truck:
    def engine(self):
        print('Truck has 12 tor generate power')


class JCB:
    def engine(self):
        print('JCB has 20 tor generate power')


if __name__ == '__main__':

    while True:
        vehicle = input('Object type : ')
        if vehicle == 'break': break
        obj = eval(vehicle+'()')
        obj.engine()

