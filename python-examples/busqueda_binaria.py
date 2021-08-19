import random

def busqueda_binaria(lista, comienzo, final,objetivo):
    print(f"buscando {objetivo} entre {lista[comienzo]} y {lista[final -1]}")
    if comienzo > final:
        return False
    
    medio = (comienzo + final)//2
    print(f"{comienzo}--{final}")
    print(f"{lista[medio]} -- {objetivo}")
    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        lista[medio] > objetivo
        
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)


if __name__ == '__main__':
    tamanio_lista = int(input('De que tamaño es la lista? '))
    objetivo = int(input('Que número quieres encontrar? '))
    lista = sorted([random.randint(0,100) for i in range(tamanio_lista)])
    encontrado = busqueda_binaria(lista,comienzo=0,final= len(lista), objetivo=objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
