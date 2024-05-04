class Menu:
    __opciones: dict
    
    def __init__(self) -> None:
        self.__opciones = {}
        
    def mostrarMenu(self, opciones):
        self.__opciones.clear()
        self.__opciones.update(opciones)
        print('\n**Menú de Opciones**\n')
        for indice, valor in self.__opciones.items():
            print(f'{indice}: {valor}')
        print('\n')
            
            