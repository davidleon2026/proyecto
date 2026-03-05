from Punto import * #importamos todo

class Recta: #creamos la clase
        def __init__(self, p1, p2=Punto(0, 0)): #para crear la recta necesitamos dos puntos
        #parametros en minus
        #p2 = Punto(0, 0) -> indica que si no se da p2 este será (0, o)
            """
            :param p1:
            :param p2:

            >>> R1 = Recta(Punto(2, 3), Punto(4, 5))
            >>> print(R1.P2)
            (4, 5)
            >>> R2 = Recta(Punto(2, 3))
            >>> print(R2.P2)
            (0, 0)
           """
            if (isinstance(p1, Punto) and isinstance(p2, Punto) and p1 != p2):
                self.P1 = p1
                self.P2 = p2
            else:
                raise "Error fatal"
        def m(self):
            return ((self.P1.y - self.P2.y) /
                    (self.P1.x - self.P2.x))
        def b(self):
            pass
        def perpendicular(self, P):
            pass
        def intersection(self, R2):
            pass
        def distancia(self, P):
            if self.pasa.(P):
                return 0
            perp = self.perpendicular(P)
            pint = self.intersection(perp)
            return P.distancia(pint)
        def pasa(self, P):
            pass
if __name__ == "__main__":
        import doctest
        print(doctest.testmod())
