class RemoveChar:

    @staticmethod
    def remove_char(a, i):
        str_data = ''
        for inx in range(len(a)):
            if i-1 != inx:
                str_data += a[inx]
        return str_data


if __name__ == '__main__':
    data = input('Enter : ')
    index = int(input('Index : '))
    output = RemoveChar.remove_char(data, index)
    print(output)
    