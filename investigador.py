from personal import Personal

class Investigador (Personal):
    __areaInvest: str
    __tipoInvest: str

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvest, tipoInvest, carrera='', cargo='', catedra='', categoria='') -> None:
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra, areaInvest, tipoInvest, categoria)
        self.__areaInvest = areaInvest
        self.__tipoInvest = tipoInvest

    def __str__(self) -> str:
        s = f'Cuil: {super().getCuil()}, apellido {super().getApellido()}, nombre: {super().getNombre()}, sueldo Basico: {super().getSueldoBasico()}, antiguedad: {super().getAntiguedad()}, area de investigacion: {self.__areaInvest}, tipo de investigacion: {self.__tipoInvest}'
        return s

    def getAreaInvestigacion (self):
        return self.__areaInvest

    def getTipoInvestigacion (self):
        return self.__tipoInvest