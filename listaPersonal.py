from nodo import Nodo
from personal import Personal
from docInv import docenteInvestigador
from investigador import Investigador
from coleccion import IColeccion

class listaPersonal (IColeccion):
    __comienzo: Nodo
    __actual: Nodo
    __indice = 0
    __top = 0

    def __init__(self) -> None:
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__top = 0

    def __str__(self) -> str:
        for personal in self:
            print (personal)

    def __iter__ (self):
        self.__actual = self.__comienzo
        return self

    def __next__ (self):
        if self.__actual is None or self.__indice == self.__top:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def buscarAnterior (self, i):
        nodoAnterior = self.__comienzo
        while self.__indice < i:
            nodoAnterior = nodoAnterior.getSiguiente()
            self.__indice += 1
        return nodoAnterior

    def agregarElemento(self, elemento):
        nodo = Nodo (elemento)
        nodo.setSiguiente (self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__top += 1
        print ('Se agregó el personal!')

    def insertarElemento(self, elemento, posicion):
        if posicion < 0 or posicion > self.__top:
            raise ValueError ('Posición inválida')
        if posicion == 0:
            self.agregarElemento(elemento)
            
        else:
            self.__indice = 0
            nodoAnterior = self.buscarAnterior(posicion)
            nuevo = Nodo(elemento)
            sig = nodoAnterior.getSiguiente()
            nuevo.setSiguiente(sig)
            nodoAnterior.setSiguiente(Nodo)
            self.__actual = nuevo
            self.__top += 1
            print ('Se agregó el personal!')
            self.__indice = 0

    def mostrarElemento(self, posicion):
        if posicion < 0 or posicion > self.__top:
            raise ValueError ('Posicion invalida')
        if posicion == 0:
            print (f'Tipo de agente: {type(self.__comienzo)}')
        else:
            for dato in self:
                if self.__indice == posicion:
                    print (f'Tipo de agente: {type(dato)}')

    def listaOrdenada (self, carr):
        docentes = []
        for dato in self:
            if isinstance (dato, docenteInvestigador) and dato.getCarrera() == carr:
                docentes.append(dato)
        if len (docentes) > 0:
            docentes.sort(key=lambda x: x.getNombre())
        else:
            raise ValueError (f'No hay docentes en la carrera: {carr}')
        return docentes

    def contarAreaInvest (self, ai):
        contadores = {'docInv': 0, 'total': 0}
        for dato in self:
            if isinstance (dato, Investigador) and dato.getAreaInvestigacion() == ai:
                contadores['total'] += 1
            if isinstance (dato, docenteInvestigador) and dato.getAreaInvestigacion() == ai:
                contadores['docInv'] += 1
        return contadores

    def ordenarPorApellido (self):
        agentes = []
        for dato in self:
            agentes.append(dato)
        agentes.sort(key=lambda x: x.getApellido())
        return agentes

    def calcularPorcentajeAntiguedad (self, a):
        return  a.getAntiguedad() * a.getSueldoBasico() / 100

    def calculoCargo (self, a):
        valorRetorno = 0
        if a.getCargo() == 'simple':
            valorRetorno = 10 * a.getSueldoBasico() / 100
        elif a.getCargo() == 'semiexclusivo':
            valorRetorno = 20 * a.getSueldoBasico() / 100
        else: valorRetorno = 50 * a.getSueldoBasico() / 100
        return valorRetorno

    def calcularCategoria (self, a):
        valorRetorno = 0
        if a.getCategoria() >= 1 and a.getCategoria() <= 10:
            valorRetorno = 10 * a.getCategoria() / 100
        elif a.getCategoria() >= 11 and a.getCategoria() <=20:
            valorRetorno = 20 * a.getCategoria() / 100
        else: valorRetorno = 30 * a.getCategoria() / 100
        return valorRetorno

    def calcularSueldo (self, a):
        valorRetorno = 0
        if a.__class__.__name__ == 'Docente':
            ant = self.calcularPorcentajeAntiguedad(a)
            cargo = self.calculoCargo(a)
            valorRetorno = a.getSueldoBasico() + ant + cargo
        elif a.__class__.__name__ == 'deApoyo':
            ant = self.calcularPorcentajeAntiguedad(a)
            cat = self.calcularCategoria(a)
            valorRetorno = a.getSueldoBasico() + ant + cat
        elif a.__class__.__name__ == 'Investigador':
            ant = self.calcularPorcentajeAntiguedad(a)
            valorRetorno = a.getSueldoBasico() + ant
        else:
            valorRetorno = a.getSueldoBasico() + a.getImporte()
        return valorRetorno

    def calcularTotalImporte (self, cat):
        total = 0
        for a in self:
            if isinstance (a, docenteInvestigador) and a.getCategoria() == cat:
                print (f'''
Apellido: {a.getApellido()}
Nombre: {a.getNombre()}
Importe extra por docencia e investigación: ${a.getImporte()}''')
                total += a.getImporte()
        return total

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            personal=[personal.toJSON() for personal in self]
            )
        return d


