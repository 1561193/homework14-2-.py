def test_info(*args, **kwargs):
    print(args)
    for i, arg in enumerate(args):
        print('Позиционный параметр:', i, arg )
    print(kwargs)
    for key, value in kwargs.items():
            print('Именованный аргумент:', key, '=', value)


test_info(59, 'Андрей', True, пёс="Умка", порода= 'Алабай')

# Ещё один вариант

def test(*args, names_autor="Andr", **kwargs):
    print('Данные:', kwargs)
    for key, n in kwargs.items():
        print(key, n)
    print(args)


test('Пример использования:', 1, 2, 3, 4, names_author='Andr', name='Andrey', course='Pyton')


def factorial(n):
    if n == 1:
        return 1
    a = factorial(n=n -1)
    return n * a
print(factorial(10))




