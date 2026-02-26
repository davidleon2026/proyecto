def resta(a,b):
    """
    :param a:
    :param b:
    :return: a - b
    >>> resta(4,1)   #doctest para probar funcion
    3
    >>> resta(1,4)   #doctest para probar funcion
    -3
    """
    return a-b

# print(resta(4,1))

if __name__ == '__main__':
    import doctest
    doctest.testmod()