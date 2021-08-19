#1.- Comenzar a hacer comparaciones de elementos adyacentes
#2.- Repetir hasta tener una pasada completa sin ningun swap

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        print(array)
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]

array = [190,1200,1,2,4,55,100,6,800]
bubble_sort(array)

print("El arreglo ordenado de forma ascendente es:")
for i in range(len(array)):
    print("%d"%array[i]),
    
            
        
