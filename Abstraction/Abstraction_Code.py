from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def information(self):
        pass

class BMW(Car):

    def information(self):
        print('This is BMW X series car')


if __name__ == '__main__':
    BMW().information()