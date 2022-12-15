def args_func(*args):
    for item in args:
        print(item)


def kwargs_func(**kwargs):
    for idx, item in kwargs.items():
        print(idx, ' : ', item)


def func(a, b, c):
    print(a, b, c)


args_func('hello', 'hii', 'bye')
kwargs_func(id=11001, name='John', salary=35000)
l = [1, 2, 3]
func(*l)
d = {'a': 11001, 'b': 'Shubham', 'c': 35000}
func(**d)

