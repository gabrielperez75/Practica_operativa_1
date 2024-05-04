from claseCliente import Cliente
import csv


class ManejadorCliente:
    __listaClientes = list
    
    def __init__(self) -> None:
        self.__listaClientes = []
        
        
    def cargarLista(self):
        try:
            
            with open('ClientesFarmaCiudad.csv', 'r') as listado:
                datosC = csv.reader(listado, delimiter= ';')
                
                next(datosC)
                for linea in datosC:
                    # print(linea)
                    linea[4] = float(linea[4])
                    linea[3] = int(linea[3])
                    cliente = Cliente(*linea)    
                    self.__listaClientes.append(cliente) 
                
        except FileExistsError:
            print('archivo no encontrado')
            
    
    def getListaClientes(self):
        return self.__listaClientes
    
    
    def buscarNumCta(self, dni):
        encontrado = False
        i = 0
        while encontrado == False and i < len(self.__listaClientes):
            if dni == self.__listaClientes[i].get_dni():
                encontrado = self.__listaClientes[i]
            else:
                i +=1
                
        return encontrado
       
            
    def mostrarDatos(self, cuenta, movimiento):
        
        print(f"""
              Apellido y Nombre: {cuenta.get_apellido()} {cuenta.get_nombre()}
              Movimientos:
              Fecha\t\tDescripción\t\t\tImporte\t    Tipo de movimiento
              
              """)
        for movim in movimiento.getArreglo():
            if cuenta.get_cuenta() == movim.get_numCta():
                print(f'\t\t{movim.get_fecha()}\t{movim.get_descripcion():20}\t\t{movim.get_importe()}\t\t{movim.get_tipoMovto()}')
    
    def actualizarSaldos(self, cuenta, instanciaMov, instanciaCliente):
        importe = 0
        
        for movimiento in instanciaMov.getArreglo():
            # print(f'numero de cuenta en clientes {cuenta.get_cuenta()} numero de cuenta en movimientos {movimiento.get_numCta()}')
            # print(type(cuenta.get_cuenta()))
            # print(type(movimiento.get_numCta()))
            if cuenta.get_cuenta() == movimiento.get_numCta():
                # print(f'SON IGUALES!!! numero de cuenta en clientes {cuenta.get_cuenta()} numero de cuenta en movimientos {movimiento.get_numCta()}')
                if movimiento.get_tipoMovto() == 'P':
                    # print(f'es pago por {movimiento.get_importe()}')
                    importe -= movimiento.get_importe()
                    # print(f'importe vale {importe}')
                elif movimiento.get_tipoMovto() == 'C':
                    # print(f'compra por {movimiento.get_importe()}')
                    importe += movimiento.get_importe()
                    # print(f'importe vale {importe}')
                        
        # print(importe)
        cuenta.set_saldo(importe)
        # print(cuenta.get_saldo())
        # print(cuenta)
        # print(movimiento)
        
        instanciaCliente.mostrarDatos(cuenta, instanciaMov)

                                
            