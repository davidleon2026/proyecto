from Punto import *
class Recta:
    def __init__(self, p1, p2=Punto(x:0, y:0)):
        """
        : param p1:
        : param p2:
        >>> R1 = Recta(Punto(2, 3), Punto(4, 5))))
        >>>print(R1.P2)
        (4,5)
        >>> R2 = Recta(Punto(2, 3))
        >>>print(R2.P2)
        (0,0)
        """
        if (isinstance(p1,Punto) and isinstance(p2,Punto) and p1 != p2):
            self.P1 = p1
            self.P2 = p2
        else:
            raise TypeError("Punto incorreto")

        def m(self):
            return ((self.P1.y - self.P2.y) / (self.P1.x - self.P2.x))
        def b(self):
            pass
        def perpendicular(self, P):
            pass

        def interseccion(self, P):
            try:

        def distancia(self, P):
            if self.pasa(P):
                return 0
            perp= self.perpendicular(P)
            self.interseccion(perp)
            pint= self.interseccion(perp)
            return P.distancia(pint)
            pass
        def pasa(self, P):
            pass

        if __name__ == "__main__":
            import doctest
            print(doctest.testmod())
