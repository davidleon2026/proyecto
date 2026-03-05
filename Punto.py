#las clases se escriben con mayus: Punto
#el criterio para separar objetos en diferentes clases es personal
class Punto:
    def __init__(self, x, y):
        self.x = x #self es el objeto, self.x es el atributo
        self.y = y #y es un parametro, un valor dado. Lo que se conserva es self.y

    def modulo(self):
        return (self.distancia(Punto(0, 0)))

    def distancia(self, otro):
        if isinstance(otro, Punto): #comprobamos si otro tiene lo mismo que Punto
                                    # si es mismo tipo i contiene lo mismo, en ete caso (x,y) validos
            return(((self.x - otro.x)**2+(self.y - otro.y)**2)**0.5)
        else:
            raise NotImplementedError("Punto no valido") #devuelves un error si no funciona

    def cuadrante(self):
        if self.x >= 0 and  self.y >= 0:
            return 1                #tras return escribir if, no else o elif
        if self.x < 0 and self.y > 0:
            return 2
        if self.x < 0 and self.y < 0:
            return 3
        return 4
    def medio(self, Q):
        if isinstance(Q,Punto):
            return Punto((self.x + Q.x)//2,
                         (self.y + Q.y)//2)
        raise NotImplementedError("Punto no valido")

if __name__ == '__main__':
    P = Punto(0, 0) #valores aleatorio
    print(P.x) #no se puede hacer print(x), esta no esta definida(daria error)
    Q = Punto(2, 2) #valores aleatorio
    print(Q.modulo())
    print(P.distancia(Q)) #P es self, Q es otro
    print(P.cuadrante())
    print(Q.cuadrante())
    try:
            print(P.distancia(2))
    except NotImplementedError as e:
        print(f"error:{e}")
    R= print(P.medio(Q)
    print(type(R))
    print(R.x, R.y))

    def __str__(self):
        """
        >>> R1 = Punto(0, 0)
        >>> print(R1)
        (0, 0)
        :param self:
        :return:
        """
        return f"(: {self.x}, {self.y})"
    def __eq__(self, other):
        """

        :param other:
        :return:
        >>> R1 = Punto(0, 0)
        >>> R2 = Punto(0, 0)
        >>> print(R1 == R2)
        True
        >>>R3 = Punto(1, 0)
        >>>R1 == R3
        False
        >>> R1 != R3
        True
        """
        return self.x == other.x and self.y == other.y
if __name__ == "__main__":
    import doctest
    print(doctest.testmod(verbose=True))