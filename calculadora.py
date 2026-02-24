def resta (a,b):
    """
    Parameters
    ----------
    a: number
       un sumando
    b: number
       otro sumando

    Returns
    -------
        la suma de a  y b

    """
    return a - b

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(sumar(4,5))
    print(resta(4,5))