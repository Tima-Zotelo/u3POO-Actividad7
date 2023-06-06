from personal import Personal

class Nodo:
    __personal: Personal
    __siguiente: object

    def __init__(self, personal) -> None:
        self.__personal = personal
        self.__siguiente = None

    def __str__(self) -> str:
        return str (self.__personal)

    def setSiguiente (self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente (self):
        return self.__siguiente

    def getDato (self):
        return self.__personal