def test_(*args):
    print(test_)
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('позиция:', i, arg)


test_(4, 'как дела?', True)


def fac(n):
    if n == 1:
        return 1
    return fac(n-1) * n


print(fac(6))