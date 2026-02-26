def suma(a,b):
    """
    :param a:
    :param b:
    :return: a + b
    >>> suma(2,1)   #doctest para probar funcion
    3               #resultado que deberia dar doctest
    """
    return a+b
print(suma(1,2))
#usar doctest en codigo

if __name__ == '__main__':
    import doctest
    doctest.testmod()