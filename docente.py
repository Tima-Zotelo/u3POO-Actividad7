from personal import Personal

class Docente (Personal):
    __carrera: str
    __cargo: str
    __catedra: str

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, carrera='', cargo='', catedra='', areaInvest='', tipoInvest='', categoria='') -> None:
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra, areaInvest, tipoInvest, categoria)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra

    def __str__(self) -> str:
        s = f'Cuil: {super().getCuil()}, apellido {super().getApellido()}, nombre: {super().getNombre()}, sueldo Basico: {super().getSueldoBasico()}, antiguedad: {super().getAntiguedad()}, carrera: {self.__carrera}, cargo: {self.__cargo}, catedra: {self.__catedra}'
        return s

    def getCarrera (self):
        return self.__carrera

    def getCargo (self):
        return self.__cargo

    def getCatedra (self):
        return self.__catedra