'''
O Doctest onde os testes são escritos no docstring e
depois executado.
Acredito que se a função for sucinta vale a pena colocar
ou usar enquanto programa para não se perder.

'''


def soma(x, y):
    '''Soma x e Y no Doctests

    >>> soma(10, 20)
    30

    >>> soma('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: X tem que ser int ou float
    '''
    assert isinstance(x, (float, int)), 'X tem que ser int ou float'
    assert isinstance(y, (float, int)), 'Ytem que ser int ou float'

    return x + y


def subtrai(x, y):
    '''Subtrair x e y
    >>> subtrai(10, 5)
    5

    >>> subtrai('10', 5)
    Traceback (most recent call last):
    ...
    AssertionError: X tem que ser int ou float
    '''

    assert isinstance(x, (float, int)), 'X tem que ser int ou float'
    assert isinstance(y, (float, int)), 'Ytem que ser int ou float'

    return x - y


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
