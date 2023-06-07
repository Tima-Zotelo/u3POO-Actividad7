from personal import Personal

class deApoyo (Personal):
    __categoria: int

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, categoria, carrera='', cargo='', catedra='', areaInvest='', tipoInvest='') -> None:
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra, areaInvest, tipoInvest, categoria)
        self.__categoria = categoria

    def __str__(self) -> str:
        s = f'Cuil: {super().getCuil()}, apellido {super().getApellido()}, nombre: {super().getNombre()}, sueldo Basico: {super().getSueldoBasico()}, antiguedad: {super().getAntiguedad()}, categoria: {self.__categoria}'
        return s

    def getCategoria (self):
        return self.__categoria