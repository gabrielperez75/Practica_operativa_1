import numpy as np
import csv
from claseMovimiento import *
from claseCliente import *

class GestorMovimiento:
    __arreglo_movimientos: np.array
    
    def __init__(self) -> None:
        self.__arreglo_movimientos = np.array([])
        
        
    def cargaArreglo(self):
        
        try:
            
            with open('MovimientosAbril2024.csv', 'r') as archivo:
                
                movimientos = csv.reader(archivo, delimiter=';')
                next(movimientos)
                
                for linea in movimientos:
                    # print(linea)
                    linea[0] = int(linea[0])
                    linea[4] = float(linea[4])
                    movimiento = Movimiento(*linea)
                    
                    self.__arreglo_movimientos = np.append(self.__arreglo_movimientos, movimiento)
                    
        except FileExistsError:
             print('archivo no encontrado')
             
    def getArreglo(self):
        return self.__arreglo_movimientos
    
    
    def ordenarArreglo(self):
        self.__arreglo_movimientos.sort()
        
    
    def getArreglo(self):
        return self.__arreglo_movimientos
    
    
    def buscarFecha(self, cuenta, cliente):
        abril = False
        # print(type(cliente))
        # print(cuenta)
        for movimiento in self.__arreglo_movimientos:
            for persona in cliente.getListaClientes():
                if persona.get_cuenta() == cuenta:
                    mes = movimiento.get_fecha().split('/')
                    if mes[1] == '4':
                        abril = True
        if abril == False:
            print(f'{persona.get_apellido()} {persona.get_nombre()}')
                
        
        
        
    def __str__(self):
        for cuenta in self.__arreglo_movimientos:
            print(cuenta.get_numCta())
            
