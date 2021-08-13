def multiplicar_por_dos(n):
    return n*2


def sumar_dos(n):
    return n+2


def aplicar_operacione(function, numeros):
    resultados = []
    for numero in numeros:
        resultado = function(numero)
        resultados.append(resultado)
    return resultados
nums = [1,2,3]

resultado = aplicar_operacione(multiplicar_por_dos, nums)
print (f"El resultado es: {resultado}")

def presetarse(nombre):
    return f"Me llamo {nombre}"


def estudiemos_juntos(nombre):
    return f"¡Hey {nombre}, aprendamos Python"


def consume_funciones(funcion_entrante):
    return funcion_entrante("Eddy")

def funcion_mayor():
    print("Esta es una función mayor y su mensaje de salida.")

    def librerias():
        print("Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.")

    def frameworks():
        print("Algunas frameworks de Python son: Django, Flask")
	
    frameworks()
    librerias()
