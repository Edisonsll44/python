#Buscar rl número menor en mi array
#Crear dos subarrays para llevar el control de mi algoritmos para
#Imprimir el resultado del ordenamiento
import sys
array=[10,3,7,100,44,234,90,1,66,156,25,522]

def selection_sort(array):
    #recorrer todo el array
    for i in range(len(array)):
        print (array)
        #Encontrar el valor minimo restante de nuestro array desordenado
        idxDes = i
        for j in range(i+1, len(array)):
            if array[idxDes] > array[j]:
                idxDes = j

        #ya que encontramos el minimo lo vamos a cambiar
        #por el primer valor de nuestro array desordenado
        array[i],array[idxDes] = array[idxDes],array[i]


 #ejecutar la funcion
selection_sort(array)
print ("Array ordenado:")
for i in range(len(array)):
    print("%d"%array[i]),