class Cliente:
    __nombre: str
    __apellido: str
    __dni: str
    __numCta: int
    __saldoAnt: float
    
    
    
    def __init__(self,nombre ,apelido ,dni ,cuenta, saldo ) -> None:
        self.__nombre = nombre
        self.__apellido = apelido
        self.__dni = dni
        self.__numCta = cuenta
        self.__saldoAnt = saldo
     
    def set_saldo(self, importe):
        self.__saldoAnt += importe
    
    
    def get_saldo(self):
        return self.__saldoAnt

    
    def get_dni(self):
        return self.__dni
    
    
    def get_apellido(self):
        return self.__apellido
    
    
    def get_nombre(self):
        return self.__nombre
    
    
    def get_cuenta(self):
        return self.__numCta
    
    
   
 
   