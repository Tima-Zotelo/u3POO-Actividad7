from nodo import Nodo
from personal import Personal
from coleccion import IColeccion

class listaPersonal (IColeccion):
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __top: int

    def __init__(self) -> None:
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__top = 0

    def __str__(self) -> str:
        for personal in self:
            print (personal)

    def __iter__ (self):
        return self

    def __next__ (self):
        if self.__indice == self.__top:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def agregarElemento(self, elemento):
        nodo = Nodo (elemento)
        nodo.setSiguiente (self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__top += 1

    def insertarElemento(self, elemento, posicion):
        ''

    def mostrarElemento(self, posicion):
        ''