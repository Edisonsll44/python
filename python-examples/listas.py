def ejemplo_listas():
    mi_lista = list(range(100))
    print(mi_lista)
    doblar = [i * 2 for i in mi_lista]
    print(doblar)
    pares = [i for i in mi_lista if i % 2 == 0]
    print(pares)

def run():
    ejemplo_listas()


if __name__ == "__main__":
    run()