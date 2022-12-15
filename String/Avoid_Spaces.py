class Avoid_Spaces:

    @staticmethod
    def avoid_spaces(a):
        count = 0
        for n in range(len(a)):
            if a[n] != ' ':
                count += 1
        return count


if __name__ == '__main__':
    data = input('Enter : ')
    length = Avoid_Spaces.avoid_spaces(data)
    print(len(data))
    print(length)
