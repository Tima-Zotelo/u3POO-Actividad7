from docente import Docente
from investigador import Investigador

class docenteInvestigador (Docente, Investigador):
    __cat: str
    __importe: int

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra, areaInvest, tipoInvest, cat, importe, categoria='') -> None:
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra, areaInvest, tipoInvest, categoria)
        self.__cat = cat
        self.__importe = importe

    def __str__(self) -> str:
        s = f'Cuil: {super().getCuil()}, apellido {super().getApellido()}, nombre: {super().getNombre()}, sueldo Basico: {super().getSueldoBasico()}, antiguedad: {super().getAntiguedad()}, carrera: {super().getCarrera()}, cargo: {super().getCargo()}, catedra: {super().getCatedra()}, area de investigacion: {super().getAreaInvestigacion()}, tipo de investigacion: {super().getTipoInvestigacion()}, categoria: {self.__cat}, importe: {self.__importe}'
        return s

    def getCategoria (self):
        return self.__cat

    def getImporte (self):
        return int (self.__importe)