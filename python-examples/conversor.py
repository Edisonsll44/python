def conversor(tipo_pesos,valor_dolar):
    pesos = input("¿Cuantos pesos " +tipo_pesos+ " tienes?: ")
    pesos = float(pesos)
    valor_dodale = valor_dolar
    dolares = pesos/valor_dodale
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
    

menu = """
Bienvenido al conversor de monedas

1- Pesos colombianos
2- Pesos argentinos
3- Pesos mexicanos

Elige una opción: """

opcion =int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinosnos",3875)
elif opcion == 3:
    conversor("mexicanos", 3875)
else:
    print("Ingrese una opción correcta por favor")