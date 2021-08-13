poblacion_pais = {
        "Argentina": 44_938_712,
        "Brasil": 210_147_125,
        "Colombia":12_234_665
    }

def run():

    agregar_elemento_diccionario("Ecuador")
    eliminar_elemento("Colombia")
    print(validar_existencia("Chile"))
    mi_diccionario = {
      "llave1": 1,
      "llave2": 2,
      "llave3": 3  
    }
   
    for pais in poblacion_pais.keys():
        print(pais)

    for pais1 in poblacion_pais.values():
        print(pais1)

    for pais, poblacion in poblacion_pais.items():
        print(pais + " tiene: " + str(poblacion) + " habitantes")


def buscar_diccionario(pais, poblacion):
    return poblacion_pais.get(pais,poblacion)

def agregar_elemento_diccionario(pais):
    poblacion_pais[pais] = 1200000


def eliminar_elemento(pais):
    del poblacion_pais[pais]

def validar_existencia(pais):
    return pais in poblacion_pais


if __name__ == "__main__":
    run()