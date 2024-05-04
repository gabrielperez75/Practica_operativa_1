from gestorCliente import *
from gestorMovimientos import *
from claseMenu import *

if __name__ == '__main__':
    
    instanciaGCliente = ManejadorCliente()
    instanciaGMovimiento = GestorMovimiento()
    instanciaGCliente.cargarLista()
    instanciaGMovimiento.cargaArreglo()
    menu = Menu()
    continuar = True
    menuPrincipal = {'0': 'Finalizar' ,'1': 'Actualizar Saldos', '2': 'Mostrar Nombre y apellido', '3': 'Odenar Gestos Movimientos'}
    while continuar:
        menu.mostrarMenu(menuPrincipal)
        opcion = input('ingrese la opción deseada: ')
        # print(instanciaGMovimiento)
        
        if opcion == '0':
            print('\nGracias por usar nuestro software\n')
            continuar = False
            
        elif opcion == '1':
            """actualiza saldos de cuentas"""
            dni = input(' dni del cliente: ')
            cuenta = instanciaGCliente.buscarNumCta(dni)
            if cuenta == False:
                print('No se encontrú el cliente')
            else:
                # print(f'los datos que obtuve de la búsqueda {cuenta}')
                instanciaGCliente.actualizarSaldos(cuenta, instanciaGMovimiento, instanciaGCliente)
        
        
        elif opcion == '2':
            
            dni = input(' dni del cliente: ')
            cuenta = instanciaGCliente.buscarNumCta(dni)
            if cuenta == False:
                print('No se encontró el cliente')
            else:
                instanciaGMovimiento.buscarFecha(cuenta.get_cuenta(), instanciaGCliente)
                
            
        
        elif opcion == '3':
            # for instancia in instanciaGMovimiento.getArreglo():
            #     print(f'antes de ordenar{instancia.get_numCta()}')
            instanciaGMovimiento.ordenarArreglo()
            # for instancia in instanciaGMovimiento.getArreglo():
            #     print(f'despues de ordenar{instancia.get_numCta()}')
        
        else:
            print('debe ingresar una opción válida')
            
            