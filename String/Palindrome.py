class Palindrome:

    @staticmethod
    def palindrome(a):
        reverse = a[::-1]
        if a == reverse:
            return True
        else:
            return False


if __name__ == '__main__':
    data = input('Enter : ')
    flag = Palindrome.palindrome(data)
    if flag:
        print('String is Palindrome')
    else:
        print('String is not Palindrome')

