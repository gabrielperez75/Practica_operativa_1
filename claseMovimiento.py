from datetime import datetime, date
class Movimiento:
    __numCta: int
    __fecha: date
    __descripcion: str
    __tipoMovto: str
    __importe: float
    
    def __init__(self, numCta, fecha, descripcion, tipoMovto, importe) -> None:
        self.__numCta = numCta
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tipoMovto = tipoMovto
        self.__importe = importe
        
    def get_numCta(self):
        return self.__numCta
    
    def get_fecha(self):
        return self.__fecha
    
    def get_descripcion(self):
        return self.__descripcion
    
    def get_tipoMovto(self):
        return self.__tipoMovto
    
    def get_importe(self):
        return self.__importe
    
    
    def __lt__(self, otro):
        return int(self.__numCta) < int(otro.get_numCta())
    