class Interchange:

    @staticmethod
    def interchange(a):
        a[0], a[-1] = a[-1], a[0]
        return a


if __name__ == '__main__':
    data = [12, 45, 83, 23, 34]
    print('Before   :', data)
    output = Interchange.interchange(data)
    print('After    :', output)
