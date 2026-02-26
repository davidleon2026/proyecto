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
        print(e)