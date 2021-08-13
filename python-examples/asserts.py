def primera_letra(lista_palabras):
    primera_letra=[]

    for palabra in lista_palabras:
        try:
            assert type(palabra) == str, f"{palabra} no es String"
            assert len(palabra) > 0, "No se permiten vacios"
            primera_letra.append(palabra[0])
        except AssertionError as e:
            print(e)
    
    return primera_letra

lista = ["Angel", 5.5,"",2,"12345678", 0.2345]
print(f"Primeras letras validas son: {primera_letra(lista)}")