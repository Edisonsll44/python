import random

def ordenamiento_por_mezcla(lista):
    pass


if __name__ == '__main__':
    tamanio_lista = int(input("De que tamaño sera la lista? "))
    lista = [random.randint(0,100) for i in range(tamanio_lista)]
    print(lista)
    print("-"*20)
    
    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)    