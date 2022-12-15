class Reverse_words:

    @staticmethod
    def revers(a):
        list_data = a.split()[::-1]

        # s = ''
        # for item in list_data:
        #     s += item+' '
        # return s

        str_data = ' '.join([item for item in list_data])
        return str_data


if __name__ == '__main__':
    data = input('Enter : ')
    output = Reverse_words.revers(data)
    print(output)

"""reverse using single line"""
# print(' '.join(input('Enter : ').split()[::-1]))
