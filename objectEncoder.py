import json
from pathlib import Path
from listaPersonal import listaPersonal
from docente import Docente
from investigador import Investigador
from deApoyo import deApoyo
from docInv import docenteInvestigador

class ObjectEncoder(object):

    def decodificarDiccionario(self, d, lp):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'listaPersonal':
                personal = d['personal']
                listaPersonal = class_()
                for i in range(len(personal)):
                    xPersonal = personal[i]
                    class_name = xPersonal.pop('__class__')
                    class_ = eval(class_name)
                    atributos = xPersonal['__atributos__']
                    unPersonal = class_(**atributos)
                    lp.agregarElemento(unPersonal)
            return listaPersonal

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
            print ('Se guardó el archivo correctamente')

    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding = "UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)