import os
from docente import Docente
from deApoyo import deApoyo
from investigador import Investigador
from docInv import docenteInvestigador

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1: self.opc1,
                            2: self.opc2,
                            3: self.opc3,
                            4: self.opc4,
                            5: self.opc5,
                            6: self.opc6,
                            7: self.opc7,
                            8: self.opc8,
                            99: self.mostrar,
                            0: self.salir
                        }
        
    def opcion(self,op, lp, oe):   ##manejador == manejador de la clase enviada desde el main
        func=self.__switcher.get(op, lambda: print("Opción no válida, intente de nuevo"))
        if op == 1 or op == 2 or op == 3 or op == 4 or op == 5 or op ==6 or op == 7 or op == 8 or op == 99:
            func(lp, oe)
        else:
            func()

    def mostrarMenu(self):
        print("""
---------->Menu Principal<----------

-> 1: Insertar personal
-> 2: Agregar Personal
-> 3: Ver tipo de agente guardado en una posicion
-> 4: Generar un listado de docentes investigadores
-> 5: Ver cantidad de agentes por area de investigacion
-> 6: Generar un listado ordenado por apellido
-> 7: Listar docentes investigadores por categoria
-> 8: Guardar datos
-> 0: Salir del programa
""")

## OPCIONES

    def cargaAutomatica (self, lp, oe):
        os.system('cls')
        dic = oe.leerJSONArchivo ('Personal.json')
        lp = oe.decodificarDiccionario (dic, lp)

    def cargarPersonal (self):
        print("""
-> 1: Docente
-> 2: Investigador
-> 3: Personal de apoyo
-> 4: Docente investigador
""")
        opcion = int (input("Su opcion: "))
        cuil = input ('Ingrese cuil: ')
        ape = input ('Ingrese Apellido: ')
        nom = input ('Ingrese Nombre: ')
        sB = int (input ('Ingrese sueldo básico: '))
        ant = int (input ('Ingrese antigúedad: '))
        if opcion == 1:
            carrera = input ('Ingrese carrera: ')
            cargo = input ('Ingrese cargo (simple, semiexclusivo, exclusivo): ')
            catedra = input ('Ingrese catedra: ')
            xPersonal = Docente (cuil, ape, nom, sB, ant, carrera, cargo.lower(), catedra)
        elif opcion == 2:
            areaInvest = input ('Ingrese area de investigacion: ')
            tipoInvest = input ('Ingrese tipo de investigacion: ')
            xPersonal = Investigador (cuil, ape, nom, sB, ant, areaInvest.lower(), tipoInvest)
        elif opcion == 3:
            categoria = input ('Ingrese categoria: ')
            xPersonal = deApoyo (cuil, ape, nom, sB, ant, categoria)
        elif opcion == 4:
            carrera = input ('Ingrese carrera: ')
            cargo = input ('Ingrese cargo (simple, semiexclusivo, exclusivo): ')
            catedra = input ('Ingrese catedra: ')
            areaInvest = input ('Ingrese area de investigacion: ')
            tipoInvest = input ('Ingrese tipo de investigacion: ')
            cat = input ('Ingrese categoria: ')
            importe = int (input ('Ingrese importe: '))
            xPersonal = docenteInvestigador (cuil, ape, nom, sB, ant, carrera, cargo.lower(), catedra, areaInvest.lower(), tipoInvest, cat.upper(), importe)
        else: 
            print ('Opcion ingresado invalido, vuelva a intentarlo')
            self.cargarPersonal()
        return xPersonal

    def opc1 (self, lp, oe):
        os.system('cls')
        print ('---------->Insertar personal<----------')
        index = int (input ('Ingrese posicion: '))
        personal = self.cargarPersonal ()
        lp.insertarElemento (personal, index)

    def opc2 (self, lp, oe):
        os.system('cls')
        print ('---------->Ageregar personal<----------')
        personal = self.cargarPersonal()
        lp.agregarElemento(personal)

    def opc3 (self, lp, oe):
        os.system('cls')
        print ('---------->Tipo de agrente<----------')
        index = int (input ('Ingrese posicion: '))
        lp.mostrarElemento (index)

    def opc4 (self, lp, oe):
        os.system('cls')
        print ('---------->Lista de docentes investigadores<----------')
        carrera = input ('Ingrese una carrera para buscar: ')
        lista = lp.listaOrdenada (carrera)
        for docente in lista:
            print (docente)
            print ('\n')

    def opc5 (self, lp, oe):
        os.system('cls')
        print ('---------->Area de investigacion<----------')
        areaInvest = input ('Ingrese area de investigacion: ')
        cont = lp.contarAreaInvest(areaInvest.lower())
        print (f'''
Cantidad de docentes investigadores: {cont['docInv']}
Cantidad de investigadores en el area: {cont['total']}
''')

    def opc6 (self, lp, oe):
        ' nombre y apellido, tipo de Agente y sueldo de todos los agentes'
        os.system('cls')
        print ('---------->Listado de agentes<----------')
        lista = lp.ordenarPorApellido()
        for a in lista:
            print (f'''
Nombre: {a.getNombre()}
Apellido: {a.getApellido()}
Tipo de agente: {a.__class__.__name__}
Sueldo: ${lp.calcularSueldo(a)}''')

    def opc7 (self, lp, oe):
        os.system('cls')
        print ('---------->Docentes investigadores<----------')
        cat = input ('Ingrese categoria (I, II, III, IV o V): ')
        total = lp.calcularTotalImporte(cat.upper())
        print (f'El total de dinero que la Secretaría de Investigación debe solicitar al Ministerio: ${total}')

    def opc8 (self, lp, oe):
        os.system('cls')
        print ('---------->Guardar datos<----------')
        op = input ('Desea guardar datos? se sobrescribiran datos actuales (s/n): ')
        if op.lower() == 's':
            d = lp.toJSON ()
            oe.guardarJSONArchivo (d, 'Personal.json')
        elif op.lower() =='n': return
        else: raise ValueError ('Error, opcion no valida')

    def mostrar (self, lp, oe):
        os.system('cls')
        for dato in lp:
            print (dato)

    def salir (self):
        print ('saliendo...')