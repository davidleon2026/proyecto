from Punto import Punto
from Recta import Recta


class Segmento(Recta):
    """"
    >>> from Punto import Punto
    >>> S = Segmento(Punto(2,3), Punto(4,5))
    >>> print(S.P2)
    (4, 5)
    >>> T = Segmento(Punto(2,3)
    >>> print(T.P2))
    (0, 0)
    """
    def longitud(self):
        return self.P1.distancia(self.P2)

    def distancia(self, P):
        if self.perpendicular(self.P1) <= P <= self.perpendicular(self.P2):
            return super().distancia(P)
        if self.perpendicular(self.P1) > P:
            return P.distancia(self.P1)
        return P.distancia(self.P2)
    def interseccion(self, otro):
        if isinstance(otro, Recta):
            Pinters = super().interseccion(otro)
            return self.interseccion(Pinters)
        if isinstance(otro, Segmento):
            Pinters = super().interseccion(otro)
            if self.interseccion(Pinters) and otro.interseccion(Pinters):
                return Pinters
        if isinstance(otro, Punto):
            return True
        return None






if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)
