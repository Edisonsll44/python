class Persona:

    def __init__(self, nombre):
        self.nombre = nombre


    def avanzar(self):
        print ("Ando camiando")


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanzar(self):
        print ("Ando moviendome en mi bicicleta")

def main():
    persona =Persona("Eddy")
    persona.avanzar()

    ciclista = Ciclista("Augusto")
    ciclista.avanzar()


if __name__ == '__main__':
    main()