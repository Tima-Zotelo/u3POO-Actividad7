class Personal:
    __cuil: str
    __apellido: str
    __nombre: str
    __sueldoBasico: int
    __antiguedad: int

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, carrera='', cargo='', catedra='', areaInvest='', tipoInvest='', categoria='') -> None:
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldoBasico = sueldoBasico
        self.__antiguedad = antiguedad

    def toJSON(self):
        if self.__class__.__name__ == 'Docente':
            d = dict(
                __class__ = self.__class__.__name__,
                __atributos__ = dict(
                    cuil = self.__cuil,
                    apellido = self.__apellido,
                    nombre = self.__nombre,
                    sueldoBasico = self.__sueldoBasico,
                    antiguedad = self.__antiguedad,
                    carrera = self.getCarrera(),
                    cargo = self.getCargo(),
                    catedra = self.getCatedra()
                )
            )
        elif self.__class__.__name__ == 'deApoyo':
            d = dict(
                __class__ = self.__class__.__name__,
                __atributos__ = dict(
                    cuil = self.__cuil,
                    apellido = self.__apellido,
                    nombre = self.__nombre,
                    sueldoBasico = self.__sueldoBasico,
                    antiguedad = self.__antiguedad,
                    categoria = self.getCategoria()
                )
            )
        elif self.__class__.__name__ == 'Investigador':
            d = dict(
                __class__ = self.__class__.__name__,
                __atributos__ = dict(
                    cuil = self.__cuil,
                    apellido = self.__apellido,
                    nombre = self.__nombre,
                    sueldoBasico = self.__sueldoBasico,
                    antiguedad = self.__antiguedad,
                    areaInvest = self.getAreaInvestigacion(),
                    tipoInvest = self.getTipoInvestigacion()
                )
            )
        else:
            d = dict(
                __class__ = self.__class__.__name__,
                __atributos__ = dict(
                    cuil = self.__cuil,
                    apellido = self.__apellido,
                    nombre = self.__nombre,
                    sueldoBasico = self.__sueldoBasico,
                    antiguedad = self.__antiguedad,
                    areaInvest = self.getAreaInvestigacion(),
                    tipoInvest = self.getTipoInvestigacion(),
                    carrera = self.getCarrera(),
                    cargo = self.getCargo(),
                    catedra = self.getCatedra(),
                    cat = self.getCategoria(),
                    importe = self.getImporte()
                )
            )
        return d

    def getCuil (self):
        return self.__cuil

    def getApellido (self):
        return self.__apellido

    def getNombre (self):
        return self.__nombre

    def getSueldoBasico (self):
        return self.__sueldoBasico

    def getAntiguedad (self):
        return self.__antiguedad