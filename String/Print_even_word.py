class Print_even_word:

    @staticmethod
    def even_word(a):
        str_data = a.split()
        str_out = ''
        for item in str_data:
            if len(item) ^ 1 == len(item) + 1:
                str_out += item+' '
        return str_out


if __name__ == '__main__':
    data = input('Enter : ')
    output = Print_even_word.even_word(data)
    print(output)
