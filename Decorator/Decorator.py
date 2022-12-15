def decor(fanc):
    def check(name):
        if not name.isalpha():
            print('Please enter valid data')
        else:
            fanc(name)
    return check


@decor
def wish(name):
    print(f'Best of luck {name}')


wish('John')
wish('1234')

decorfanction = decor(wish)
decorfanction('Shubham')
decorfanction('1111')




