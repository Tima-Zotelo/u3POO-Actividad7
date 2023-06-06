import os

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1: self.opc1,
                            2: self.mostrar,
                            3: self.opc3,
                            0: self.salir
                        }
        
    def opcion(self,op, lp, oe):   ##manejador == manejador de la clase enviada desde el main
        func=self.__switcher.get(op, lambda: print("Opción no válida, intente de nuevo"))
        if op == 1 or op == 2 or op == 3:
            func(lp, oe)
        else:
            func()

    def mostrarMenu(self):
        print("""
---------->Menu Principal<----------

-> 1: Cargar datos
-> 2: opc 2
-> 3: opc 3
-> 0: Salir del programa
""")

## OPCIONES

    def opc1 (self, lp, oe):
        os.system('cls')
        dic = oe.leerJSONArchivo ('Personal.json')
        lp = oe.decodificarDiccionario (dic, lp)

    def opc2 (self, lp, oe):
        os.system('cls')
        return

    def opc3 (self, lp, oe):
        os.system('cls')
        return

    def mostrar (self, lp, oe):
        for dato in lp:
            print (dato)

    def salir (self):
        print ('saliendo...')