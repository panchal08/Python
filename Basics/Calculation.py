class Calculation:

    @staticmethod
    def calculation(val1, val2, val3):

        if val2 == '+':
            return val1 + val3
        elif val2 == '-':
            return val1 - val3
        elif val2 == '*':
            return val1 * val3
        elif val2 == '/':
            return val1 / val3
        elif val2 == '**':
            return val1 ** val3
        elif val2 == '%':
            return val1 % val3
        else:
            return 'Enter valid data...!'


if __name__ == '__main__':

    val1 = int(input('Value : '))
    val2 = input('Operator : ')
    val3 = int(input('Value : '))

    result = Calculation.calculation(val1, val2, val3)

    print(f'Output : {result}')
